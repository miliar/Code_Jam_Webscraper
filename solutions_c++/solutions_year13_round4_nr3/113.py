#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<complex>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)
// #define dprintf(...)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

struct vertex{
	int indegree;
	int a;
	int b;
	bool oka, okb;
	int q;
};

#define MAXV 2002
vertex g[MAXV];
int edge[MAXV][MAXV];
int ea[MAXV][MAXV];
int eb[MAXV][MAXV];
int n;

priority_queue<int,vector<int>,greater<int> > pq;

void double_check(void);

int main2(int cn){
	scanf("%d", &n);
	for(int i=0; i<n; ++i) scanf("%d", &g[i].a);
	for(int i=0; i<n; ++i){
		scanf("%d", &g[i].b);
		g[i].indegree = 0;
		g[i].oka = g[i].okb=true;
		g[i].q=-1;
	};
	for(int i=0; i<n; ++i) for(int j=0; j<n; ++j){
		edge[i][j]=0;
		ea[i][j]=0;
		eb[i][j]=0;
	};
	while(!pq.empty()) pq.pop();

	for(int i=0; i<n; ++i){
		for(int j=i+1; j<n; ++j){
			if(g[i].a >= g[j].a){
				edge[j][i] = 1;
				g[i].indegree++;
			};
			if(g[i].a == g[j].a - 1){
				ea[i][j] = 1;
				g[j].oka = false;
			}
			if(g[j].b >= g[i].b){
				edge[i][j] = 1;
				g[j].indegree++;
			};
			if(g[i].b - 1 == g[j].b){
				eb[j][i] = 1;
				g[i].okb = false;
			}
		};
	};
	for(int i=0; i<n; ++i){
		if(g[i].indegree == 0 && g[i].oka && g[i].okb) {
			pq.push(i);
			g[i].q=-2;
		};
	};
	int q=0;
	while(!pq.empty()){
		int v=pq.top();
		pq.pop();

		g[v].q=q;
		q++;
		for(int i=0; i<n; ++i) {
			if(edge[v][i] && g[i].q == -1){
				g[i].indegree--;
			}
			if(ea[v][i]) g[i].oka=true;
			if(eb[v][i]) g[i].okb=true;
			if(g[i].q == -1 && g[i].indegree == 0 && g[i].oka && g[i].okb){
				pq.push(i);
				g[i].q=-2;

			};
		};
	};
	double_check();
	printf("Case #%d: ", cn);
	for(int i=0; i<n; ++i) printf("%d ", g[i].q+1);
	printf("\n");
	return 7;
};

int na[MAXV], nb[MAXV];

void double_check(void){
	for(int i=0; i<n; ++i){
		na[i]=1;
		for(int j=0; j<i; ++j) if(g[j].q < g[i].q) na[i] = max( na[i], na[j]+1 );
	};
	for(int i=n-1; i>=0; --i){
		nb[i]=1;
		for(int j=i+1; j<n; ++j) if(g[j].q < g[i].q) nb[i] = max(nb[i],
				nb[j]+1);
	};

	bool ok=true;
	for(int i=0; i<n; ++i){
		if(na[i] != g[i].a || nb[i] != g[i].b) ok=false;
	}
	if(ok) dprintf("GOOD!\n");
	else{
		dprintf("WRONG!\n");
		dprintf("Expected a:\n");
		for(int i=0; i<n; ++i) dprintf("%d ", g[i].a);
		dprintf("\nGot a:\n");
		for(int i=0; i<n; ++i) dprintf("%d ", na[i]);
		dprintf("\nExpected b:\n");
		for(int i=0; i<n; ++i) dprintf("%d ", g[i].b);
		dprintf("\nGot b:\n");
		for(int i=0; i<n; ++i) dprintf("%d ", nb[i]);
		dprintf("\n");
	};
};

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; ++i) main2(i+1);
	return 0;
}

