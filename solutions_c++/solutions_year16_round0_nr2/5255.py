#include <bits/stdc++.h>
///
///kill me PlZ !!!! i am a Shity code :( :(
//feeeling lonely in my life
///falled in love but from one side
//thing started to get really shit
///forever alone :(
using namespace std;
#define ll long long
const ll INF = (ll) LLONG_MAX;
//#define ln length()
#define pb push_back
#define sz size
#define mp make_pair
#define qq  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define all(n)   (n).begin(),(n).end()
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vll vector<pair<ll,ll> >
#define vi vector <int>
#define F first
#define S second
#define fcin(n,x) for(int i=0;i<n;cin>>x[i++])
#define fcout(n,x) for(int i=0;i<n;cout<<x[i++]<<" ")
#define cn(v) scanf("%d",&v)
#define cn2(v,w) scanf("%d %d",&v,&w)
#define cn3(v,w,z) scanf("%d %d %d",&v,&w,&z)
#define endl "\n"
#define EPS 1e-18
#define for2c(n,m,mat) for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>mat[i][j];
#define fori(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
//directions
int dx[4] = { 0, -1, 0, 1 };
int dy[4] = { 1, 0, -1, 0 };
int dx8[9] = { 1,0,-1,0,1,-1,-1,1,0 };
int dy8[9] = {  0,1,0,-1,1,-1,1,-1,0};
///commenly used function s :) :) :) : )//
//priority_queue<int, vector<int>, std::greater<int> > first;
ll ipow(ll base,ll exp)
{
    ll result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}
string tos(ll n)
{
    stringstream ss;
    string ans;
    ss << n;
    ss >> ans;
    return ans;
}
ll toll(string n)
{
    return atoll(n.c_str());
}
double dist(double x1, double y1, double x2, double y2)
{
    return sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
}
int doubleCompare(double x, double y)
{
    if (fabs(x - y) <= EPS)
        return 0;

    if (x < y)
        return -1;

    return 1;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//new code ///////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


int main()
{
//////////
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int tc;
    cin>>tc;
    for(int i=0; i<tc; i++)
    {
        string x;
        cin>>x;
        cout<<"Case #"<<i+1<<": ";

        ll ans=0;
        for(int i=1;i<x.size();i++){
            if(x[i]==x[i-1]){
                x.erase(i,1);
                i--;
            }
        }
        if(x.size()==1){
            if(x[0]=='+')cout<<0<<endl;
            else cout<<1<<endl;
        }else{
        bool flag=0;
        ll ans=0;
        for(int i=0;i<x.size();i++){
            if(!flag && x[i]=='+'){
            flag=1;
            }
            if(x[i]=='-'&&flag)ans+=2;
            if(x[i]=='-'&&!flag)ans++;

        }
        cout<<ans<<endl;
        }

    }


}
