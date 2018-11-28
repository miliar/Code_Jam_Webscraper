#include<bits/stdc++.h>
#include<string>
using namespace std;


typedef long long ll;
typedef vector<int> vi;

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

int ii = 'i';
int jj = 'j';
int kk = 'k';


int multiply(int x,int y)
{
  if(x==1 && y==1)
    return 1;
  if(x==1 && y==ii)
    return ii;
  if(x==1 && y==jj)
    return jj;
  if(x==1 && y==kk)
    return kk;


  if(x==ii && y==1)
    return ii;
  if(x==ii && y==ii)
    return -1;
  if(x==ii && y==jj)
    return kk;
  if(x==ii && y==kk)
    return -jj;

  if(x==jj  && y==1)
    return jj;
  if(x==jj && y==ii)
    return -kk;
  if(x==jj && y==jj)
    return -1;
  if(x==jj && y==kk)
    return ii;

  if(x==kk && y==1)
    return kk;
  if(x==kk && y==ii)
    return jj;
  if(x==kk && y==jj)
    return -ii;
  if(x==kk && y==kk)
    return -1;


  else
    return 1;
}

int main()
{
  freopen("C-small-attempt0.in","r",stdin);
  freopen("C-small-attempt0.out","w",stdout);


  int t;
  s(t);
  int n,x;



  for (int cas = 1; cas <= t; ++cas)
  {
    s2(n,x);
    string s,str;
    cin>>s;
    for (int i = 0; i < x; ++i)
    {
      str+=s;
    }

    int len = str.length();
    str+="$$$$";
    if(len<3)
    {
      printf("Case #%d: NO\n",cas);
      continue;
    }
    int state = 0;
    int mul = str[0];
    int posi; 
    for (int i = 1; i < len; ++i)
    {
      if(mul==ii && state==0)
      {
        state=1;
        posi = i-1;
        // cout<<i<<"  dfcdfcdc\n";
        break;

      }
      // cout<<mul<<" "<<(int)str[i]<<endl;
      if(mul>0)
      mul = multiply(mul,(int)str[i]);
      else
      mul = -multiply(-mul,(int)str[i]);

    
    }

    if(state==1)
    {
      mul = str[posi+1];


      for (int i = posi+2; i < len; ++i)
      {
      if(mul==jj)
      {
        state=2;
        posi = i-1;
        break;
      }
       if(mul>0)
      mul = multiply(mul,(int)str[i]);
      else
      mul = -multiply(-mul,(int)str[i]);

      }


    }

    if(state==2)
    {
      mul = str[posi+1];

      for (int i = posi+2; i < len; ++i)
      {
        // cout<<"hello\n";
       if(mul>0)
      mul = multiply(mul,(int)str[i]);
      else
      mul = -multiply(-mul,(int)str[i]); 
      }
      if(mul==kk)
      {
        state=3;
      }


    }


    if(state==3)
    {
      printf("Case #%d: YES\n",cas);
    }
    else
    {
      printf("Case #%d: NO\n",cas);
    }



  }
  

}

