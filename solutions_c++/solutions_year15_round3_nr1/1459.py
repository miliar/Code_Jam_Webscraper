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
int main ()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int R,C,W;
    int t;
    cin >> t;
    FOR(i,1,t+1)
    {
        cin >> R>> C >> W;
        int O =(C/W);
        if(C%W!=0)
            O++;
        int ans =(R)*O + W-1;
        printf("Case #%d: %d\n",i,ans);

    }
    return 0;

}
