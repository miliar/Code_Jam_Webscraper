
/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Vishwas Tripathi
 * CSE, MNNIT-ALLAHABAD
 * vishfrnds@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(i=0;i<n;i++)
#define REP(i,a,b) for(i=a;i<=b;i++)
#define X first
#define Y second
#define all(c) c.begin(),c.end()

#define tr(c, itr) for(itr = (c).begin(); itr != (c).end(); itr++)
//#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end()) //for set,map,etc
#define cpresent(container, element) (find(all(container),element) != container.end()) //for vectors

 typedef long long ll;
 typedef vector<int> vi;
 typedef vector< vi > vvi;
 typedef pair< int,int > ii;

#define sz(a) int((a).size())]
#define clr(a) memset(a,0,sizeof(a))
#define ini(a) memset(a,-1,sizeof(a))


//i/o
#define inp(n) scanf("%d",&n)
#define inp2(n,m) scanf("%d%d",&n,&m)
#define ins(s) scanf("%s",s);
#define out(n) printf("%d\n",n)
#define out2(n,m) printf("%d %d\n",n,m)
#define inc(n) scanf("%c",&n)

//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999

#define inll(n) scanf("%lld",&n)
#define inll2(n,m) scanf("%lld%lld",&n,&m)
#define outll(n) printf("%lld\n",n)
#define outll(n) printf("%lld\n",n)
#define outll2(n,m) printf("%lld %lld\n",n,m)

int main()
{
    int t, n, i, j, ok, minl, ans, cs,k;
    char s[110];
    inp(t);
    REP(cs, 1, t)
    {
        minl = 200;
        inp(n);
        ok = 1;
        vector<pair<int, char> > v[n];
        rep(i, n)
        {
            scanf("%s",s);
            j = 0;
            char last = -1;
            k = -1;
            while(s[j])
            {
                if(s[j] == last)
                {
                    v[i][k].X++;
                }
                else
                {
                    k++;
                    v[i].pb(MP((int)1,(char)s[j]));
                    last = s[j];
                }
                j++;
            }
            if(minl!=200 && minl!=k)
            {
                ok = 0;
                break;
            }
            minl = k;
        }
        if(!ok)
        {
           printf("Case #%d: Fegla Won\n", cs);
           continue;
        }
        ans = 0;
        rep(i, minl+1)
        {
            if(v[0][i].Y != v[1][i].Y)
            {
                ok = 0;
                break;
            }
            else
                ans += abs(v[0][i].X - v[1][i].X);
        }
        if(!ok)
        {
           printf("Case #%d: Fegla Won\n", cs);
           continue;
        }
        printf("Case #%d: %d\n", cs,ans);

    }
    return 0;
}
