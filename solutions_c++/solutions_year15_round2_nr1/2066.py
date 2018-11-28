#include<bits/stdc++.h>
using namespace std;

// #defines
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define sz(x) ((int)(x).size())
#define ms0(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
#define inf 1001001001
typedef pair<long long,long long> pii;
typedef long long ll;
typedef unsigned long long ull;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int maxn = (int)1e5 + 10;
const int mod = (int)1e9;
int fastMax(int x, int y) { return (((y-x)>>(32-1))&(x^y))^y; }
int fastMin(int x, int y) { return (((y-x)>>(32-1))&(x^y))^x; }

#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
int A[100][100];
long long rv(long long u)
{
    long long ans=0;
    while(u>0)
    {
        ans=ans*10+u%10;
        u=u/10;
    }
    return ans;
}
queue<pii> q;

int main(){
    //FILEIO("B-small-practice");
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    long long t,i,j,k,n,cnt,r,c,x;

    map<long long,bool>m;
    map<long long,long long>dp;
    cin>>t;
    dp[1]=1;
     pii p;
        p.f=1;p.s=1;
          q.push(p);
    for(i=1;i<=t;i++)
    {
        cin>>n;
        if(dp.find(n)!=dp.end())
        {
            cnt=dp[n];
            //cout<<cnt<<endl;
        }
        else
        {
       int flg=0;
       while(!q.empty()&&flg==0)
        {
          pii u=q.front();
          q.pop();
          if(u.f+1==n)
          {
              cnt=u.s+1;
             // dp[u.f+1]=u.s+1;
              flg=1;
          }
          x=rv(u.f);
          if(x==n)
          {
              cnt=u.s+1;
             // dp[x]=u.s+1;
              flg=1;
          }
          u.f=u.f+1;
          u.s=u.s+1;

          if(dp.find(u.f)==dp.end())
          {q.push(u);
           dp[u.f]=u.s;
          }
          else
          {
             dp[u.f]=min(u.s,dp[u.f]);
          }
           u.f=x;
           if(dp.find(u.f)==dp.end())
          {q.push(u);
           dp[u.f]=u.s;
          }
          else
          {
             dp[u.f]=min(u.s,dp[u.f]);
          }

        }
        //while(!q.empty())
        //q.pop();
        //m.clear();
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }

    return 0;
}


