/*
	Algorithm: Dinic'c max flow
			   using Edge List
*/

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <string.h>
#include <string>
#include <list>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <utility>

using namespace std;
#define MAX_V 300000
#define MAX_E 900000
#define INF 7777777

struct EDGE{
	int v,c;
};
int nV;
int SRC,TNK;
int eI;
EDGE Edge[MAX_E+7];	// edge list
int Next[MAX_E+7]; // next pointer of vertex v
int Last[MAX_V+7]; // last index of adj edge of vertex v
int Dist[MAX_V+7];	// level from src
int Start[MAX_V+7];// temporary used for last

inline void SetEdge( int u,int v,int c )
{
	Edge[eI].v = v;
	Edge[eI].c = c;
	Next[eI] = Last[u];
	Last[u] = eI++;
	Edge[eI].v = u;
	Edge[eI].c = 0;
	Next[eI] = Last[v];
	Last[v] = eI++;
}

int Q[MAX_V+7];
int Frnt,End;

bool Bfs( void )
{
	Frnt = End = 0;
	Q[End++] = SRC;
	int i;
	for( i=0;i<nV;i++){
		Dist[i] = INF;
	}
	Dist[SRC] = 0;
	int u,v;
	while( Frnt<End ){
		u = Q[Frnt++];
		for( i=Last[u];i!=-1;i=Next[i]){
			v = Edge[i].v;
			if( !Edge[i].c || Dist[v]<INF ) continue;
			Dist[v] = Dist[u] + 1;
			Q[End++] = v;
		}
	}
	return Dist[TNK] < INF;;
}

#define MIN( a,b ) a<b ? a:b

int AugmentPath( int u,int f )
{
	if( u==TNK ) return f;
	int Tot = 0;
	for( int &i = Start[u];i!=-1;i=Next[i] ){
		int v = Edge[i].v;
		if( !Edge[i].c ) continue;
		if( Dist[v] != Dist[u]+1 ) continue;
		int Tmp = AugmentPath( v,MIN( f,Edge[i].c ));
		Edge[i].c -= Tmp;
		Edge[i ^ 1].c += Tmp;
		Tot += Tmp;
		f -= Tmp;
		if( !f ) break;
	}
	return Tot;
}

int MaxFlow( void )
{
	int Flw = 0;
	while( Bfs()){
		memcpy( Start,Last,(nV)*sizeof(int));
		Flw += AugmentPath( SRC,2*INF );
	}
	return Flw;
}

int W,H,B;
int grid[507][507];
int In[507][507] , Out[507][507];


int inx[] = {0,0,1,-1};
int iny[] = {1,-1,0,0};

int main( void )
{
    freopen("C.in","rt",stdin);
    freopen("C.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++) {
        scanf("%d%d%d",&W,&H,&B);

        SRC = 0;
        int st = 0;
        for(int i=0;i<W;i++)
            for(int j=0;j<H;j++) {
                grid[i][j] = 0;
                st++;
                In[i][j] = st;
                st++;
                Out[i][j] = st;
            }

        st++;
        TNK = st;
        nV = TNK+1;
        eI = 0;
        memset( Last,-1,nV*sizeof(int));

        for(int i=0;i<B;i++) {
            int X1,Y1,X2,Y2;
            scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
            for(int j=min(X1,X2);j<=max(X1,X2);j++)
                for(int k=min(Y1,Y2);k<=max(Y1,Y2);k++) grid[j][k] = 1;
        }
        for(int i=0;i<W;i++)
        {
            for(int j=0;j<H;j++) {
                if(grid[i][j] == 0) {
                    SetEdge(In[i][j] , Out[i][j] , 1);
                }
                for(int k=0;k<4;k++) {
                    int nx = i + inx[k];
                    int ny = j + iny[k];
                    if(nx>=0 && nx<W && ny>=0 && ny<H) SetEdge(Out[i][j] , In[nx][ny],1);
                }
                if(j==0) SetEdge(SRC,In[i][j],1);
                if(j==H-1) SetEdge(Out[i][j],TNK , 1 );
            }
        }
        printf("Case #%d: %d\n",cas,MaxFlow());

    }


	//freopen("text1.txt","r",stdin );
	/*SRC = 0;
	TNK = N+E;
	nV = TNK+1;
	eI = 0;
	memset( Last,-1,nV*sizeof(int));*/

	return 0;
}
