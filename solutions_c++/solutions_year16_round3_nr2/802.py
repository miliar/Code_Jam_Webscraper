//Satyam Pandey :: Kamehameha //
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef long long int LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr<<name<<" : "<<arg1<<endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names,Arg1&& arg1,Args&&... args){
  const char* comma=strchr(names+1,',');
  cerr.write(names,comma-names)<<" : "<<arg1<<" | ";__f(comma+1,args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
const LL N=LL(1e18)+45;
int A[100][100];
LL R[100];
int BIT[100];
int bit(LL M)
{
  int i=0;
  while(M)
  {
    BIT[i++]=(M&1);
    M>>=1;
  }
  return i;
}
int main()
{
  int t,tt,i,j;si(t);
  R[1]=1;R[2]=1;
  LL sum=2;
  for(i=3;i<100;i++)
  {
    R[i]=sum;
    if(sum>N) sum=N;
    else sum+=R[i];
  }
  for(tt=1;tt<=t;tt++)
  {
    LL B,M;
    sll(B),sll(M);
    printf("Case #%d: ",tt);
    if(M>R[B]){
     printf("IMPOSSIBLE\n");
     continue;
    }
    else
     printf("POSSIBLE\n");
    if(B==2)
    {
      printf("01\n00\n");
      continue;
    }
    for(i=0;i<=B;i++)
      SET(A[i],0);
    int L=bit(M);
    for(i=1;i<=L+1;i++)
      for(j=i+1;j<=L+1;j++)
        A[i][j]=1;
    if(M<R[B]){
      for(i=0;i<L;i++)
        if(BIT[i])
          A[i+2][B]=1;
    }
    for(i=1;i<=B;i++){
      for(j=1;j<=B;j++)
        printf("%d",A[i][j]);
      printf("\n");
    }
  }
  return 0;
}
