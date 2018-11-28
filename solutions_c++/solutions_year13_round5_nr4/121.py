# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <iostream>
# include <vector>
# include <algorithm>
# include <queue>
# include <set>
# include <map>

using namespace std;

long double DP[21][1<<20];

int main()
{
  for(int N=1;N<=20;N++)
  {
    DP[N][(1<<N)-1]=0;
    for(int i=(1<<N)-2;i>=0;i--)
    {
      long long k=i;k|=(k<<N);

      for(int j=0;j<N;j++)
      {
        if((k&(1ll<<j))==0)
        {
          DP[N][i]+=(DP[N][i|(1ll<<j)]+N)/N;
        }
        else
        {
          for(int r=j+1;;r++)
          {
            if((k&(1ll<<r))==0)
            {
              DP[N][i]+=(DP[N][i|(1ll<<(r%N))]+N+j-r)/N;
              break;
            }
          }
        }
      }
    }
  }

  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    char inp[21];
    scanf("%s",inp);

    int N=strlen(inp),mask=0;
    for(int i=0;i<N;i++)
      if(inp[i]=='X')mask|=(1<<i);
    printf("Case #%d: %.11LE\n",t,DP[N][mask]);
  }
  return 0;
}

