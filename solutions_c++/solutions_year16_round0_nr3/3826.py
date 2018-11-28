#include <bits/stdc++.h>


using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef long double LD;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))


int dig[32];
int n,j;
bool prime[10000];
int main()
{
  prime[0]=false;
  prime[1]=false;
  bool flag;
  FOR(i,2,10000)
  {
    flag=true;
    FOR(j,2,i/2+1)
    {
      if(prime[j] && i%j==0)
      {
        flag=false;
        break;
      }
    }
    if(flag)
    {
      prime[i]=1;
      cout<<i<<endl;
    }
    else
      prime[i]=false;
  }
  prime[2]=0;

  int t;
  cin>>t;

  LL ans[11];
  REP(i,t)
  {
      CLR(dig);
      cin >> n >> j;
      dig[0]=1;
      dig[n-1]=1;
      int cou=0;
      printf("Case #%d:\n",i+1);
      while(cou<j)
      {
        flag=true;
        int k=1;
        while(1)
        {
          if(dig[k])
          {
            dig[k]=0;
            k++;
          }
          else
          {
            dig[k]=1;
            break;
          }
        }

        CLR(ans);
        FOR(k,2,11)
        {
          LL val=0;
          REP(l,n)
            val+=dig[l]*pow(k,l);

          REP(l,10000)
          {
            if(prime[l] && val%l==0)
            {
              ans[k]=l;
              break;
            }
          }
          if(ans[k]==0)
          {
            flag=false;
            break;
          }
        }
        if(flag)
        {
          REP(k,n)
            cout<<(dig[n-k-1]?1:0);
          FOR(k,2,11)
            cout<<" "<<ans[k];
          cout<<endl;
          cou++;
        }


      }
  }
}
