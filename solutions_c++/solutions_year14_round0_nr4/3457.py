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
    READ("D-large.in");
    WRITE("out.out");
    int T,w;
    vi bg;
    bg.push_back(10);

    double n[1005],k[1005];
    scanf("%d",&T);
    FOR(c,1,T)
    {
        scanf("%d",&w);
        FOR(i,0,w-1)
        scanf("%lf",&n[i]);
        FOR(i,0,w-1)
        scanf("%lf",&k[i]);
        sort(k,k+w);
        sort(n,n+w);
//        FOR(i,0,w-1)
//        printf("%.3lf ",n[i]);
//        printf("\n");
//        FOR(i,0,w-1)
//        printf("%.3lf ",k[i]);
//        printf("\n");printf("\n");
        vector<double> kw,nw;
        nw.insert(nw.begin(),n,n+w);
        kw.insert(kw.begin(),k,k+w);
        int ans2=0;
        FOR(i,0,w-1)
        {
            int ne=nw.size()-1;
            int ke=kw.size()-1;
            if(nw[ne]>kw[ke])
            {
                ans2++;
                nw.erase(nw.begin()+ne);
                kw.erase(kw.begin());
            }
            else
            {
                while(nw[ne]<kw[ke])
                {
                    ke--;
                }
                ke++;
                nw.erase(nw.begin()+ne);
                kw.erase(kw.begin()+ke);
            }

        }
        nw.insert(nw.begin(),n,n+w);
        kw.insert(kw.begin(),k,k+w);
        int ans=0;
        FOR(i,0,w-1)
        {
            int ne=nw.size()-1;
            int ke=kw.size()-1;
            if(nw[ne]<kw[ke])
            {
                nw.erase(nw.begin());
                kw.erase(kw.begin()+ke);
            }
            else
            {
                ans++;
                while(nw[ne]>kw[ke])
                {
                    ne--;
                }
                ne++;
                nw.erase(nw.begin()+ne);
                kw.erase(kw.begin()+ke);
            }

        }
        printf("Case #%d: %d %d\n",c,ans,ans2);
        kw.clear();
        nw.clear();
    }

    return 0;
}


