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
int Swap(ll a)
{
    ll res = 0;
    while(a>0)
    {
        res*=10;
        res+=a%10;
        a/=10;
    }
    return res;

}
int get( ll a)
{
    ll T = Swap(a);
    return T%10;

}
int getSize(int a)
{

    int res = 0;
    while(a>0)
    {
        res++;
        a/=10;
    }
    return res;

}
int val, S;
int dis[1000001];

int main()
{
    freopen("In.in","r",stdin);
    freopen("out.txt","w",stdout);
    memset(dis,-1,sizeof dis);
    val=1000001;
    S=getSize(val);
    queue <pi>Q;
    Q.push(mp(1,1));

    while(!Q.empty())
    {
        pi a = Q.front();
        Q.pop();
        if(dis[a.first]!=-1)
            continue;

        if(getSize(a.first)>S)
            continue ;


        dis[a.f]=a.s;
        //  cout << a.f <<endl;


        Q.push(mp(a.f + 1,a.s+1));
        Q.push(mp(Swap(a.f) , a.s+1));

    }

    //cout  << q <<endl;
    int tc;
    cin >> tc;
    FOR(t,1,tc+1)
    {

        cin >> val ;
        printf("Case #%d: ",t);

        cout << dis[val] <<endl;

    }

    return 0;

}


