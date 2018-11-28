#define PROB ""
//#define SUBMIT

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>


#pragma warning(disable:4996)
using namespace std;

#define EXIT exit(0);
#define INP(_X) scanf("%d",& _X);
#define OUT(_X) printf("%d ",_X);
#define abs(_Z) (((_Z)<0)?-(_Z):(_Z))

#define f0(_X,_Y) for((_X)=0;(_X)<(_Y);++(_X))
#define f1(_X,_Y) for((_X)=1;(_X)<=(_Y);++(_X))
#define ff(_X,_Y,_Z) for((_X)=(_Y);(_X)<=(_Z);++(_X))
#define fF(_X,_Y,_Z) for((_X)=(_Y);(_X)<(_Z);++(_X))

#define rf0(_X,_Y) for(_X=(_Y)-1;(_X)>=0;--(_X))
#define rf1(_X,_Y) for(_X=(_Y);(_X)>0;--(_X))
#define rff(_X,_Y,_Z) for(_X=(_Y);(_X)>=(_Z);--(_X))
#define rfF(_X,_Y,_Z) for(_X=(_Y);(_X)>(_Z);--(_X))

#define sz(_X) _X.size()
typedef long long ll;

#ifdef SUBMIT
    #define FIN
    #define FOUT
    #define LINE
    #define PRT(_X)
    #define DOUT(_X)
    #define DLINE
    #define TIME
#else
    #define FIN freopen("input" PROB ".txt","r",stdin);
    #define FOUT freopen("output" PROB ".txt","w",stdout);
    #define LINE printf("\n");
    #define PRT(_X) std::cout<< #_X ": "<<_X<<std::endl;
    #define DOUT(_X) fprintf(stderr,"%d ",_X);
    #define DLINE fprintf(stderr,"\n");
    #define TIME fprintf(stderr,"\n-----------\ntime : %.2f sec\n",double(clock())/CLOCKS_PER_SEC);
#endif

char a[1002][102], A[1002][102];
int choose[202][202], d[102][102];
const int MOD = 1000000007;

int comp(int i, int j)
{
    int k=0;
    while(A[i][k] && A[j][k] && A[i][k]==A[j][k]) ++k;
    return A[i][k]<A[j][k];
}

int sorted[1001],size[102][30];
int cost, ways;
int n,m;

// return its strecth
void explore(int level,int start,int end)
{
    int i, first=start;

    int stretch = std::min(end-start+1, m);
    cost += stretch;
    int g = 0;

    ff(i,start,end+1)
    {
        // new group
        if(i>end || a[first][level]!=a[i][level])
        {
            size[level][++g] = std::min(i-first, m);

            if(a[first][level])
                explore(level+1,first,i-1);
            first = i;
        }
    }

    int longest = 0;
    d[0][0]=1;
    ff(i,1,g)
    {
        stretch = size[level][i];
        longest = std::min(longest + stretch, m);

        int j; fF(j,0,stretch) d[i][j]=0;
        ff(j,stretch,longest)
        {
            d[i][j]=0;

            int k; ff(k, std::max(0, j-stretch), j)
                d[i][j] = (d[i][j]+(long long)d[i-1][k]*choose[j][k]%MOD*choose[k][stretch-(j-k)]%MOD)%MOD;
        }
        ff(j,longest+1,m) d[i][j]=0;
    }
    ways = ways*(long long)d[g][longest]%MOD;
}

int main()
{
    FIN FOUT

    int t,tc=0;

    int i;
    choose[0][0]=1;
    f1(i,200)
    {
        choose[i][0]=1;
        int j; f1(j,i) choose[i][j]=(choose[i-1][j-1]+choose[i-1][j])%MOD;
    }

    for(scanf("%d",&t);t--;)
    {
        scanf("%d%d",&n,&m);
        f1(i,n) scanf("%s",A[i]), sorted[i]=i;
        std::sort(sorted+1,sorted+n+1,comp);
        f1(i,n)
        {
            int j;
            for(j=0;A[sorted[i]][j];++j)
                a[i][j]=A[sorted[i]][j];
            a[i][j]=0;
        }

        cost=0;
        ways=1;
        explore(0,1,n);

        printf("Case #%d: %d %d\n", ++tc, cost, ways);
    }

    return 0;
}