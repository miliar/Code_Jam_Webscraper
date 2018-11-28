
#include <bits/stdc++.h>
using namespace std;

#if !ONLINE_JUDGE
#include "debug.h"
#else
#endif

#define INF 10001000100LL
#define MOD 1000000007

typedef long long int LL;
typedef unsigned long long LLU;
typedef long double LD;

#define F first
#define S second
#define PB push_back
#define MK make_pair
#define PP pop_back
#define LEN(vale) strlen(vale)
#define SZ(vale) (int)vale.size()
#define SQ(A) ((A)*(A))
#define pc putchar_unlocked
#define gc getchar_unlocked
#define FI(i12,fa,fb) for(i12=fa;i12<fb;++i12)
#define FD(i12,fa,fb) for(i12=fa;i12>fb;--i12)
#define FT(it,S) for(it = (S).begin(); it != (S).end(); ++it) 
#define bits(vale) __builtin_popcount(vale)
#define IO  ios_base::sync_with_stdio(false);  cin.tie(NULL);  cout.tie(NULL)

#define SET1(array,val,sz) for(int i13=0;i13<sz;i13++)array[i13]=val;
#define SET2(array,val,sz1,sz2) for(int i13=0;i13<sz1;i13++)for(int i14=0;i14<sz2;i14++)array[i13][i14]=val;

#define ALL(a) a.begin(),a.end()
#define LB (lower_bound)
#define UB (upper_bound)

#define SI(vale) scanf("%d",&vale)
#define PI(vale) printf("%d\n",vale)
#define PIS(vale) printf("%d ",vale)
#define SL(vale) scanf("%lld",&vale)
#define PL(vale) printf("%lld\n",vale)
#define PLS(vale) printf("%lld ",vale)
#define SS(vale) scanf("%s",vale)
#define PS(vale) printf("%s\n",vale)
#define SLD(vale) scanf("%Lf",&vale)
#define PLD(vale) printf("%0.12Lf\n",vale)
#define NL printf("\n")

typedef pair<int,int> PR;
typedef vector<int> vt;

#define TCS() int testcase; SI(testcase);while(testcase--) 
bool deb=false;
const int N=100011;
vector<int> a;

int decim(LL x,LL n)
{
       a.clear();
       while(x != 0)
       {
              a.PB(x%2);
              x/=2;
       }
       reverse(ALL(a));
       return SZ(a);
}

LL isprime(LL n)
{
       LL p = sqrt(n);
       int i;
       FI(i,2,p+1)
       {
              if(n%i == 0)
                     return i;
       }
       return -1;
}

LL basex(int x,int n)
{
       int i;LL y = 0;
       FD(i,n-1,-1)
              if(a[i] != 0)
                     y += pow(x,n-i-1);
       return y; 
}

int main(){
       //IO;
       //clock_t tStart = clock();
       LL i,j = 1,n,J,s=0; int cs=0;
       TCS(){
              cs++;s = 0;
              SL(n);SL(J);
              vector<int>ans,ANS[N];
              LL p = 1LL<<n;
              FI(i,1,p+1)
              {
                     if(decim(i,n) == n && a[0] == 1 && a[n-1] == 1)
                     {
                            bool OK = 1;
                            vector<LL>val;
                            FI(j,2,11)
                            {
                                   LL t = basex(j,n);
                //                   TR(t,j);
                                   LL ch = isprime(t);
                                   if(ch == -1)
                                   {
              //                            TR(t);
                                          OK = 0;
                                          break;
                                   }
                                   val.PB(ch);
                            }
                            if(OK == 1)
                            {
                                   ans.PB(i);
                                   FI(j,0,SZ(val))
                                          ANS[s].PB(val[j]);
                                   s++;
                            }
                     }
                     if(s == J)
                            break;
              }
              printf("Case #%d:\n",cs);
              FI(i,0,SZ(ans)) 
              {
                     vector<int> tmp;
                     while(ans[i] != 0)
                     {
                            tmp.PB(ans[i]%2);
                            ans[i]/=2;
                     }
                     reverse(ALL(tmp));
                     FI(j,0,SZ(tmp))
                            printf("%d",tmp[j]); printf(" "); 
                     FI(j,0,SZ(ANS[i]))
                            PIS(ANS[i][j]); NL;
              }
       }

       //exectime();
       return 0;        
}


