

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

#define read() freopen("A-large.in", "r", stdin)

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
int visited[10];
map<ll,int>mask;
bool allvisited()
{
    for(int i=0;i<10;i++)
        if(visited[i]==0)
        return false;
    return true;
}
int main()
{
read();
write();
int T;
int cas = 0;
sfi(T);
while(T--)
{
    ll N;
    sfl(N);
    ll N_cop = N;
    ms(visited,0);
    CASE(cas);
    int insomnia = 0;
    while(!allvisited())
    {
        ll N_p = N;
        if(mask[N_p]!=0)
        {
            insomnia = 1;
            break;
        }
        mask[N_p]++;
        while(N_p>0)
        {
            int digit = N_p%10;
            N_p/=10;
            visited[digit] = 1;
        }
        N+=N_cop;

    }
    if(insomnia)
        pf("INSOMNIA\n");
    else
    pf("%lld\n",N-N_cop);
mask.clear();


}
    return 0;
}
