#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
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
#define SZ(a) ((long)a.size())
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

inline long FastMax(long x, long y) { return (((y-x)>>(32-1))&(x^y))^y; }
inline long FastMin(long x, long y) { return (((y-x)>>(32-1))&(x^y))^x; }

long IR[] = { 0,-1,0,1,-1,-1,1,1 };
long IC[] = { 1,0,-1,0,1,-1,-1,1 };

long mat1[7][7] , mat2[7][7];
long r1,r2;

int main( void )
{
    long i,j,Icase,k=0;

    freopen("a.txt","r",stdin );
    freopen("a.out","w",stdout );

    scanf("%ld",&Icase);
    while( Icase--)
    {
        int r1,r2;
        scanf("%ld",&r1);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)   scanf("%ld",&mat1[i][j]);

        scanf("%ld",&r2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)   scanf("%ld",&mat2[i][j]);

        long Cnt = 0;
        long ans;
        for(i=1;i<=4;i++) {
            for(j=1;j<=4;j++) {
                if(mat1[r1][i] == mat2[r2][j]) {
                    Cnt++ ;
                    ans = mat1[r1][i];
                }
            }
        }
        if(Cnt==1) printf("Case #%ld: %ld\n",++k,ans);
        else if(Cnt>1) printf("Case #%ld: Bad magician!\n",++k);
        else printf("Case #%ld: Volunteer cheated!\n",++k);

    }



    return 0;
}

