

/****************************************

@_@
Cat Got Bored *_*
#_#
*****************************************/

#include <bits/stdc++.h>


#define loop(i,s,e) for(int i = s;i<=e;i++) //including end point

#define pb(a) push_back(a)

#define sqr(x) ((x)*(x))

#define CIN ios_base::sync_with_stdio(0); cin.tie(0);

#define ll long long

#define ull unsigned long long

#define SZ(a) int(a.size())

#define read() freopen("B-large.in", "r", stdin)

#define write() freopen("large_output.txt", "w", stdout)


#define ms(a,b) memset(a, b, sizeof(a))

#define all(v) v.begin(), v.end()

#define PI acos(-1.0)

#define pf printf

#define sfi(a) scanf("%d",&a);

#define sfii(a,b) scanf("%d %d",&a,&b);

#define sfl(a) scanf("%lld",&a);

#define sfll(a,b) scanf("%lld %lld",&a,&b);

#define mp make_pair

#define paii pair<int, int>

#define padd pair<dd, dd>

#define pall pair<ll, ll>

#define fs first

#define sc second

#define CASE(t) printf("Case #%d: ",++t) // t initialized 0

#define INF 1000000000   //10e9

#define EPS 1e-9


using namespace std;

int main()
{
    read();
    write();
    int tc;
    int cas = 0;
    sfi(tc);
    while(tc--)
    {

        string ss;
        cin>>ss;
        CASE(cas);
        int ans = 0;
        if(ss.length()==1)
        {
            if(ss[0]=='-')
                ans++;
            pf("%d\n",ans);
            continue;
        }
        int last = ss.length() - 1;
        loop(idx,1,last)
        {
            if(ss[idx]!=ss[idx-1])
                ans++;
            if(idx==last && ss[last]=='-')
                ans++;

        }
        pf("%d\n",ans);

    }


    return 0;
}
