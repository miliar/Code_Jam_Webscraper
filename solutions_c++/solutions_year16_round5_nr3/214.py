#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <stack>
using namespace std;

int N,S,x[3][1010],v[3][1010];

struct edge{
	int x,y,d;
	bool operator <(const edge &t) const{return d < t.d;}
}E[1000000];

int par[1010];

int find(int x)
{
	if (par[x] != x) par[x] = find(par[x]);
	return par[x];
}

void proc()
{
	scanf ("%d %d",&N,&S);
	for (int i=0;i<N;i++){
		for (int k=0;k<3;k++) scanf ("%d",&x[k][i]);
		for (int k=0;k<3;k++) scanf ("%d",&v[k][i]);
	}

	int c = 0;
	for (int i=0;i<N;i++) for (int j=i+1;j<N;j++){
		E[c].x = i; E[c].y = j; E[c].d = 0;
		for (int k=0;k<3;k++) E[c].d += (x[k][i] - x[k][j]) * (x[k][i] - x[k][j]);
		c++;
	}

	for (int i=0;i<N;i++) par[i] = i;
	sort(E,E+c);
	for (int i=0;i<c;i++){
		int x = find(E[i].x);
		int y = find(E[i].y);
		if (x != y){
			par[x] = y;
			if (find(0) == find(1)){
				printf ("%.12lf\n",sqrt(E[i].d));
				break;
			}
		}
	}
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);
		proc();
	}

	return 0;
}