#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<assert.h>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<utility>
#include<algorithm>
#include<list>
using namespace std;

#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define SZ(a) ((Long)a.size())
#define ALL(a) a.begin(),a.end()
#define FOREACH(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define AREA2(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define SQR(x) ((x)*(x))
#define STR string
#define IT iterator
#define ff first
#define ss second
#define MP make_pair
#define EPS 1e-9
#define INF 1000000007

#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))

typedef long long Long;
typedef vector<long> Vl;
typedef vector<Long> VL;
typedef pair<long,long> Pll;
typedef pair<Long,Long> PLL;
typedef long long Long;

#define MAX_V 200007
#define MAX_E 10*MAX_V

struct EDGE{
	long v,c;
};
long nV;
long CNST,SRC,TNK;
long eI;
EDGE Edge[MAX_E+7];	// edge list
long Next[MAX_E+7]; // next pointer of vertex v
long Last[MAX_V+7]; // last index of adj edge of vertex v
long Dist[MAX_V+7];	// level from src
long Start[MAX_V+7];// temporary used for last

inline void SetEdge( long u,long v,long c1,long c2 = 0 )
{
	Edge[eI].v = v;
	Edge[eI].c = c1;
	Next[eI] = Last[u];
	Last[u] = eI++;
	Edge[eI].v = u;
	Edge[eI].c = c2;
	Next[eI] = Last[v];
	Last[v] = eI++;
}

long Q[MAX_V+7];
long Frnt,End;

bool Bfs( void )
{
	Frnt = End = 0;
	Q[End++] = SRC;
	long i;
	for( i=0;i<nV;i++){
		Dist[i] = INF;
	}
	Dist[SRC] = 0;
	long u,v;
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

long AugmentPath( long u,long f )
{
	if( u==TNK ) return f;
	long Tot = 0;
	for( long &i = Start[u];i!=-1;i=Next[i] ){
		long v = Edge[i].v;
		if( !Edge[i].c ) continue;
		if( Dist[v] != Dist[u]+1 ) continue;
		long Tmp = AugmentPath( v,MIN( f,Edge[i].c ));
		Edge[i].c -= Tmp;
		Edge[i ^ 1].c += Tmp;
		Tot += Tmp;
		f -= Tmp;
		if( !f ) break;
	}
	return Tot;
}

long MaxFlow( void )
{
	long Flw = 0;
	while( Bfs()){
		memcpy( Start,Last,(nV)*sizeof(long));
		Flw += AugmentPath( SRC,2*INF );
	}
	return Flw;
}

#define MAX 1007

long W,H,B;
bool blk[MAX+7][MAX+7];

long IND( long x, long y )
{
    return y*W+x+1;
}

int main( void )
{
    long i,j,x1,y1,x2,y2,Icase,k,Kase = 0;

    //freopen("text1.txt","r",stdin );
    freopen("c.in","r",stdin );
    freopen("c.out","w",stdout );

    scanf("%ld",&Icase );
    while( Icase-- ){
        scanf("%ld%ld%ld",&W,&H,&B );
        CLR( blk );
        for( i=1;i<=B;i++ ){
            scanf("%ld%ld%ld%ld",&x1,&y1,&x2,&y2 );
            while( x1<=x2 ){
                long ty1 = y1;
                while( ty1<=y2 ){
                    blk[x1][ty1] = true;
                    ty1++;
                }
                x1++;
            }
        }
        CNST = W*H;
        SRC = 0;
        TNK = 2*CNST+1;
        nV = TNK+1;
        eI = 0;
        SET( Last );
        for( i=0;i<W;i++ ){
            for( j=0;j<H;j++ ){//printf("%ld\n",IND( i,j ) );
                if( blk[i][j] ) continue;
                SetEdge( IND( i,j ), CNST+IND( i,j ), 1, 0 );
                long IX[] = { 0,-1,0,1 };
                long IY[] = { 1,0,-1,0 };
                for( k=0;k<4;k++ ){
                    long ni = i+IX[k];
                    long nj = j+IY[k];
                    if( ni<0 or ni>=W or nj<0 or nj>=H ) continue;
                    if( blk[ni][nj] ) continue;
                    SetEdge( CNST+IND( i,j ), IND( ni,nj ), INF, 0 );
                }
            }
        }
        for( i=0;i<W;i++ ){//printf("here\n");
            if( !blk[i][0] ) SetEdge( SRC,IND( i,0 ),INF, 0 );
            if( !blk[i][H-1] ) SetEdge( CNST+IND( i,H-1 ),TNK,INF,0 );
        }
        long ans = MaxFlow();
        printf("Case #%ld: %ld\n",++Kase,ans );
    }

    return 0;
}
