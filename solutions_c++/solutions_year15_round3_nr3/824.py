#include <bits/stdc++.h>
using namespace std;

#define FOR(p,star,end) for(int p = star ; p<end ; p++)
#define FORR(p,star,end) for(int p = star ; p>=end ; p--)
#define INF 1000000000
#define MOD 1000000007
#define MAX 101
#define LOGMAX 14
#define pi pair<int ,int >
#define vi vector<int>
#define vp vector< pair<int ,int> >
#define vii vector< vector<int> >
#define vip vector<vector<pair<int , int > > >
#define pb push_back
#define mp make_pair
#define ll long long
#define sz(v) ((int)v.size())
#define f first
#define s second
#define EPS 10-7

using namespace std;
vi coins ;
bool Can(int loc , int rem)
{
    if(rem<0)
        return 0;

    if(loc==coins.size())
        return rem==0;
    return Can(loc+1,rem-coins[loc]) | Can(loc+1,rem);
}
int main ()
{

    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int  t;
    cin >> t;
    FOR(tc,1,t+1)
    {
        coins.clear();
        int c , d, v,a;
        cin >> c >> d >> v ;
        FOR(i,0,d)
        {
            cin >> a;
            coins.pb(a);
        }
        FOR(i,1,v+1)
        {
            if(!Can(0,i))
            {
                coins.pb(i);
                sort(coins.begin(),coins.end());

            }
        }

        printf("Case #%d: %d\n",tc,coins.size()-d);
    }


}
