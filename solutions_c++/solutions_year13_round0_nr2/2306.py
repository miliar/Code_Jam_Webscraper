#define ll long long
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("B-large.in","r",stdin)
#define filew() freopen("Blarge.txt","w",stdout)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <queue>


using namespace std;


#define NN 102

int R[NN],C[NN],A[NN][NN];

int main()
{

   // filer();
  //  filew();


    int T;

    scanf("%d",&T);


    int n,m,i,j,ks;

    FOR(ks,1,T)
    {


        scanf("%d%d",&n,&m);

        SET(R,-1);
        SET(C,-1);

        REP(i,n)REP(j,m)
        {
            scanf("%d",&A[i][j]);
            R[i]=MAX( R[i],A[i][j] );
            C[j]=MAX( C[j],A[i][j] );
        }

        bool f=1;
        REP(i,n)REP(j,m)
        {
            if(A[i][j]==R[i] || A[i][j]==C[j])continue;
            f=0;
        }


        printf("Case #%d: ",ks);

        if(f)printf("YES\n");
        else printf("NO\n");

    }


    return 0;
}


