#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;

#define PI acos(-1.0)
#define MAX 10000007
#define EPS 1e-9
#define mem(a,b) memset(a,b,sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define FOR(i, b, e) for(int i = b; i <= e; i++)
#define pr(x) cout<<x<<"\n"
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double,double> pdd;
typedef pair<ll , ll > pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<ll > vl;

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction


int main()
{
    //READ("A.in");
    READ("A-small-attempt0.in");
    WRITE("out.out");
    int T;
    scanf("%d",&T);
    FOR(i,1,T)
    {
        int f,s,fn[5][5],sn[5][5];
        vi r;
        scanf("%d",&f);
        FOR(j,1,4)
          FOR(k,1,4)
            scanf("%d",&fn[j][k]);
        scanf("%d",&s);
        FOR(j,1,4)
          FOR(k,1,4)
            scanf("%d",&sn[j][k]);

        FOR(j,1,4)
           FOR(k,1,4)
           {
               if(fn[f][j]==sn[s][k])r.pb(sn[s][k]);
           }
        printf("Case #%d: ",i);
        if(r.size()==1)printf("%d\n",r[0]);
        else if(r.size()>1)printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
        r.clear();

    }

    return 0;
}


