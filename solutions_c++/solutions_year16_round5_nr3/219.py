#include<bits/stdc++.h> 

using namespace std;

const int MAXN = 2e4 + 10;

typedef pair<int, int> PII;
typedef long long ll;

int x[MAXN], y[MAXN], z[MAXN];
int vx[MAXN], vy[MAXN], vz[MAXN]; 

double D[1111][1111];
int n;
int vis[MAXN];

double sqr(double x){
	return x * x;
}

double dis(int p, int q){
	return sqrt(sqr(x[p] -x[q]) + sqr(y[p] - y[q]) + sqr(z[p] - z[q]));
}

int check(double u){
	for(int i = 0; i <= n; i++)
		vis[i] = 0;
	vis[1] = 1;
	queue<int> Q;
	while(!Q.empty()) Q.pop();
	Q.push(1);
	while(!Q.empty()){
		int x = Q.front();
		Q.pop();
		if (x == 2)
			return 1;
		for(int i = 1; i <= n; i++)
			if (D[x][i] <= u && !vis[i]){
				Q.push(i);
				vis[i] = 1;
			}
	}
	return 0;
}

int main(){
	freopen("Cs1.in", "r", stdin);
	freopen("Cs1.out", "w", stdout);
	int T;
	cin>>T;
	for(int o = 1; o <= T; o++){
		printf("Case #%d: ", o);
		int s;
		cin>>n>>s;
		for(int i = 1; i <= n; i++){
			scanf("%d%d%d", &x[i], &y[i], &z[i]);
			scanf("%d%d%d", &vx[i], &vy[i], &vz[i]);
		}
		x[0] = y[0] = z[0] = 0;
		for(int i = 0; i <= n; i++)
			for(int j = 0; j <= n; j++)
				D[i][j] = dis(i, j);
		double low = 0, high = dis(1, 2), mid;
		for(int _ = 1 ; _ <= 100; _++){
			mid = (high + low) / 2;
			if (check(mid))
				high = mid;
			else
				low = mid;
		}
		printf("%.16f\n", (high+low)/2);
	}	
	return 0;
}
