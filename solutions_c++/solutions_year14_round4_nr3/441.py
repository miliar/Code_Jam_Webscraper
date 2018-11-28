#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

struct edge{
    edge(){
        x = y = flow = capa = 0;
    }
    edge(int x_, int y_, int c_){
        x = x_; y = y_; flow = 0; capa = c_;
    }
    int x,y,flow,capa;
}E[10000000]; int ecnt;
typedef edge* edgep;
vector<edgep> grp[4500000],rev[4500000];
int ex[4500000];

void in(int x, int y, int c)
{
    E[ecnt] = edge(x,y,c);
    grp[x].push_back(E+ecnt);
    rev[y].push_back(E+ecnt);
    ecnt++;
}

int V;

struct phase{
    phase(int x_, int m_, int c_, edgep u_){
        x = x_; m = m_; c = c_; u = u_;
    }
    int x,m,c; edgep u;

    bool operator <(const phase t) const{return c + ex[x] > t.c + ex[t.x];}
};
int dist[4500000]; edgep via[4500000];
const int non = 0x7fffffff;

int ans()
{
    int ret = 0;
    while (1){
        for (int i=0;i<V;i++) dist[i] = non;

        priority_queue<phase> Q;
        Q.push(phase(0,0x7fffffff,0,NULL));
		int fl;

        while (!Q.empty()){
            int x = Q.top().x, m = Q.top().m, c = Q.top().c; edgep u = Q.top().u; Q.pop();

            if (dist[x] <= c) continue;
            dist[x] = c;
            via[x] = u;
            if (x == V-1){
				fl = m;
				break;
			}

            for (edgep e : grp[x]){
                if (dist[e->y] == non && e->flow < e->capa){
                    Q.push(phase(e->y,min(m,e->capa-e->flow),c+1,e));
                }
            }

            for (edgep e : rev[x]){
                if (dist[e->x] == non && e->flow > 0){
                    Q.push(phase(e->x,min(m,e->flow),c+1,e));
                }
            }
        }
		if (dist[V-1] == non) break;

        int x = V-1;
        while (via[x] != NULL){
            if (via[x]->x == x){
                via[x]->flow -= fl;
                x = via[x]->y;
            }
            else{
                via[x]->flow += fl;
                x = via[x]->x;
            }
        }
        ret += fl;
    }

    return ret;
}

int X1[1010],Y1[1010],X2[1010],Y2[1010];
bool draw[1010][2020];
vector<int> Y;
int W,H,B;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test);
	for (int Case=1;Case<=Test;Case++){
		Y.clear();
		scanf ("%d %d %d",&W,&H,&B);
		for (int i=0;i<B;i++){
			scanf ("%d %d %d %d",&X1[i],&Y1[i],&X2[i],&Y2[i]);
			Y.push_back(Y1[i]);
			Y.push_back(Y2[i]+1);
		}
		Y.push_back(0); Y.push_back(H);
		for (int i=0;i<H;i++) Y.push_back(i);
		sort(Y.begin(),Y.end());
		Y.erase(unique(Y.begin(),Y.end()),Y.end());
		for (int i=0;i<W;i++) for (int j=0;j<Y.size();j++) draw[i][j] = 0;
		for (int i=0;i<B;i++){
			int j = lower_bound(Y.begin(),Y.end(),Y1[i]) - Y.begin();
			while (Y[j] <= Y2[i]){
				for (int x=X1[i];x<=X2[i];x++) draw[x][j] = 1;
				j++;
			}
		}
		int bd = W * (Y.size() - 1);
		V = bd * 2 + 2;
		for (int i=0;i<W;i++){
			if (!draw[i][0]) in(0,i*(Y.size()-1)+1,1);
			if (!draw[i][Y.size()-2]) in((i+1)*(Y.size()-1)+bd,V-1,1);
		}
		//for (int j=Y.size()-2;j>=0;j--,puts("")) for (int i=0;i<W;i++) putchar( draw[i][j] ? 'Y' : 'N');
		for (int i=0;i<W;i++) for (int j=0;j+1<Y.size();j++) if (!draw[i][j]){
			int dx[4] = {0,1,0,-1};
			int dy[4] = {1,0,-1,0};
			for (int k=0;k<4;k++){
				int px = i + dx[k];
				int py = j + dy[k];
				if (px < 0 || py < 0 || px >= W || py+1 >= Y.size()) continue;
				if (!draw[px][py]) in(i*(Y.size()-1)+j+bd+1,px*(Y.size()-1)+py+1,k%2?1:Y[j+1]-Y[j]);
			}
			in(i*(Y.size()-1)+j+1,i*(Y.size()-1)+j+bd+1,Y[j+1]-Y[j]);
		}

		for (int i=0;i<V;i++) ex[i] = 1;
		queue<int> Q;
		Q.push(V-1); ex[V-1] = 0;
		while (!Q.empty()){
			int x = Q.front(); Q.pop();
			for (edgep e : rev[x]) if (ex[e->x] == -1){
				Q.push(e->x); ex[e->x] = ex[x] - 1;
			}
		}
		//for (int i=0;i<ecnt;i++) printf ("%d %d\n",E[i].x,E[i].y);

		printf ("Case #%d: %d\n",Case,ans());
		ecnt = 0;
		for (int i=0;i<V;i++){
			grp[i].clear();
			rev[i].clear();
		}
	}

	return 0;
}