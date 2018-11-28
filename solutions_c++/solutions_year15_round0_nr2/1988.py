#include<bits/stdc++.h>
#include<string>
using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define s(n)                        scanf("%d",&n)
#define s2(q,w)                        scanf("%d %d",&q,&w)
#define s3(q,w,e)                        scanf("%d %d %d",&q,&w,&e)
#define pb(x)            push_back(x)

#define INF                         (int)1e9
#define EPS                         1e-9

#define checkbit(n,b)                ( (n >> b) & 1)

int mod = 10000007;

long long pwr(long long a,long long b,long long mod)
{
  if(b==0)
    return 1;
  long long temp=pwr(a,b/2,mod);
  temp=(temp*temp)%mod;
  if(b&1)
    temp=(temp*a)%mod;
  return temp;
}
long long pwr(long long a,long long b)
{
  if(b==0)
    return 1;
  long long temp=pwr(a,b/2);
  temp=(temp*temp);
  if(b&1)
    temp=(temp*a);
  return temp;
}
bool* isPrime;
void generatePrimeSieve(const int lim)
{
  isPrime=(bool *)malloc(lim+1);
  memset(isPrime,true,lim+1);
  isPrime[0]=false;
  isPrime[1]=false;
  for(int i=2;i<=lim;++i)
    if(isPrime[i])
      for(int j=i+i;j<=lim;j+=i)
        isPrime[j]=false;
}
#define matrix vector<vector<int> >
matrix identityMatrix;
matrix mul(const matrix &a,const matrix &b)
{
  int n=a.size();
  matrix ans(n,vector<int> (n) );
  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j < n; ++j)
    {
      for (int k = 0; k < n; ++k)
      {
        ans[i][j]+= ((long long)a[i][k]*b[k][j])%mod;
        ans[i][j]%=mod;
      }
    }
  }
  return ans;
} 
matrix pwr(const matrix &a,long long n)
{
    if(n==0)
    {
      /*define identity */
      assert(false);
      return identityMatrix;
    }
    if(n==1)
     return a;
    matrix tmp=pwr(a,n/2);
    tmp=mul(tmp,tmp);
    if(n&1)
      tmp=mul(a,tmp);
    return tmp;
}
long long gcd(long long a,long long b)
{
  return b==0?a:gcd(b,a%b);
}
long long lcm(long long a,long long b)
{  
  return (a/gcd(a,b))*b;
}
long long modularInverse(long long a,long long m)
{
      return pwr(a,m-2,m);
}
int n;
int dp[1005][1005];
int a[1005];


int dpfunc(int x,int y)
{
  if(x==y)
    return 0;

  if(x<y)
    return 0;

  if(2*y>=x)
  {
    return 1;
  }
  if(dp[x][y]!=-1)
    return dp[x][y];

  // cout<<x<<" "<<y<<endl;
  int op1=INF;

  for (int i = 1; i < x; ++i)
  {
    int rem = x-i;
    op1 = min(op1,1 + dpfunc(i,y) + dpfunc(rem,y));
  }


   
  return dp[x][y] = op1;

}



int func(int x)
{
  int ans = 0;
  for (int i = 0; i < n; ++i)
  {
    if(a[i]>x)
    {
      ans+=dpfunc(a[i],x);
    }
  }
  return ans;
}


int main()
{

  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);



  int t;
  s(t);
  memset(dp,-1,sizeof dp);

  for(int j = 1; j <= t; ++j)
  {
    s(n);
  // cout<<dpfunc(9,3)<<endl;

    int mx=0;
    for (int i = 0; i < n; ++i)
    {
      s(a[i]);
      if(a[i]>mx)
        mx=a[i];
    }
    int ans = INF;
    for (int i = 1; i <= mx ; ++i)
    {
      ans = min(ans,i+func(i));
      // cout<<i<<" "<<func(i)<<endl;
    }
    printf("Case #%d: %d\n",j,ans);

  }
  

}

