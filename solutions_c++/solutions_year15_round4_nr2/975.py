#include <bits/stdc++.h>
using namespace std;

const int N = 110;
const double eps = 1e-8;
const int M = 4000;
int head[N];
int d[N], cur[N];
int st[M], s, e, no;
double X, V;
int n;
struct point{
	int u, v,  next;
	double flow;
	point(){};
	point(int x, int y, int z, double w):u(x), v(y), next(z), flow(w){};
}p[M];
void add(int x, int y, double z){
	p[no] = point(x, y, head[x], z);	head[x] = no++;
	p[no] = point(y, x, head[y], 0);	head[y] = no++;
}
void init(){
	memset(head, -1, sizeof(head));
	no = 0;
}

int dcmp(double x){
    if(fabs(x) < eps)   return 0;
    return x > 0 ? 1 : -1;
}
bool bfs(){
	int i, x, y;
	queue<int>q;
	memset(d, -1, sizeof(d));

	d[s] = 0;	q.push(s);
	while(!q.empty()){
		x = q.front();	q.pop();
		for(i = head[x]; i != -1; i = p[i].next){
			if(dcmp(p[i].flow)> 0 && d[y = p[i].v] < 0){
				d[y] = d[x] + 1;
				if(y == e)	return true;
				q.push(y);
			}
		}
	}
	return false;
}
double dinic(){
	int i, loc, top, x = s;
	double nowflow, maxflow = 0;
	while(bfs()){
		for(i = s; i <= e; i++)	cur[i] = head[i];
		top = 0;
		while(true){
			if(x == e){
				nowflow = 1e12;
				for(i = 0; i < top; i ++){
					if(dcmp(nowflow - p[st[i]].flow) > 0){
						nowflow = p[st[i]].flow;
						loc = i;
					}
				}
				for(i = 0; i < top; i++){
					p[st[i]].flow -= nowflow;
					p[st[i]^1].flow += nowflow;
				}
				maxflow += nowflow;
				top = loc;	x = p[st[top]].u;
			}
			for(i = cur[x]; i != -1; i = p[i].next)
				if( dcmp(p[i].flow) > 0 && d[p[i].v] == d[x] + 1) break;
			cur[x] = i;
			if(i != -1){
				st[top ++] = i;
				x = p[i].v;
			}
			else {
				if(!top)	break;
				d[x] = -1;
				x = p[st[--top]].u;
			}
		}
	}
	return maxflow;
}
double r[N], t[N];
bool gao(double mid){
    int i;
    s = 0;  e = n + 2;
    init();
    add(n + 1, e, V * X);
    for(i = 1; i <= n; i++){
        add(s, i, V*X);
        add(i, n + 1, mid * r[i] * t[i]);
    }
    double temp =  dinic();
    printf("%.10f %.10f\n", temp, temp - V*X);
    if(fabs(temp - V* X) < 1e-6 ) return true;
    return false;

}


int main(){
    int TC, tc, i, y;
    double minv;
    scanf("%d", &TC);
    for(tc = 1; tc<=TC; tc++){
        scanf("%d", &n);
        scanf("%lf%lf", &V, &X);
        minv = 1e12;
        for(i = 1; i <= n; i++){
            scanf("%lf%lf", &r[i], &t[i]);
            minv = min(r[i], minv);
        }

        double low = 0.0000001, high = V/minv + 1, ans, mid;
        printf("%f\n", high);
        bool ok = false;
        while(dcmp(high - low) > 0){
            mid = (low + high) / 2;
            if(gao(mid)){
                ok = true;
                ans = mid;
                high = mid ;
            }else low = mid;
        }
        printf("Case #%d: ", tc);
        if(ok){
            printf("%.10f\n", ans);
        }else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
