//Khagan

#include <algorithm>
#include <string.h>
#include <stdio.h>
#define  maxn      1003
using    namespace std;

int T,n;
char s[maxn];

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("cikti.txt","w",stdout);
  scanf("%d",&T);
  for(int t=1 ; t<=T ; t++)
  {
    scanf("%d%s",&n,s);
    int sum=0,ans=0;
    for(int i=0 ; i<=n ; i++)
    {
      if(sum<i)
      {
        ans+=i-sum;
        sum=i;
      }
      sum+=s[i]-'0';
    }
    printf("Case #%d: %d\n",t,ans);
  }
  return 0;
}
