#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
#define all(x)         x.begin(),x.end()
#define vi             vector<int>
#define vvi            vector<vector<int> >
#define gcd            ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
#define INF            2147483647
#define LIMIT          1000
#define mod            1000000007
#define pi             pair<int,int>
#define mp             make_pair
#define pb(v)          v.push_back
#define sz(x)          x.size()

string tostr(ll x)
{ stringstream ss; ss << x; return ss.str(); }
ll toint(string &s)   
{ stringstream ss; ss << s; long long x; ss >> x; return x; }

map<pair<ll,int>,ll> h;
 vector<ll> mot(101);
ll solve(ll a,int j,int n)
{
//     cout<<"n"<<n<<endl;
         if(j>=n||j<0)
         {
           return 0;
         }
         if(a==1)
         {
            return n;
         }
         
         if(h.find(mp(a,j))!=h.end())
         {
            return h[mp(a,j)];
         }
         ll ret=0;
         if(mot[j]<a)
         {
              ret= solve(a+mot[j],j+1, n);
         }
         else if(a==1)
         {
            ret=solve(a,j+1,n)+1;
         }
         else if(mot[j]==1)
         {
               ret=solve(a,j+1,n)+1;
         }
         
         else
         {
          //cout<<"here"<<endl;
                 ll op1=0;
                ll ta=a;
                ll c1=a-1;
                while(ta<=mot[j])
                {
                   ta+=(ta-1);
                   //cout<<ta<<endl;
                   op1++;
              //     cout<<"bye"<<endl;
                   
                }
                ta+=mot[j];
                ret= min(solve(ta,j+1,n) +op1,solve(a,j+1,n)+1);
         }
         h[mp(a,j)]=ret;
         //cout<<ret<<endl;
         return ret;   
}
int main()

{
    
     freopen("in1.in","r",stdin);
     freopen("out1.out","w",stdout);
    int t,n;
    ll a;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
          cin>>a>>n;
         
          for(int i=0;i<n;i++)
          {
            cin>>mot[i];
          }
          sort(mot.begin(),mot.begin()+n);
          h.clear();
          ll ops=solve(a,0,n);
         cout<<"Case #"<<ii<<": "<<ops<<endl;
          
    }
   
    return 0;
}
