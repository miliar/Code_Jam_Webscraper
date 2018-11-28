#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long int llint;
int ary[102];
int main(void)
{
  int tc,cs,m,n,i,j,ans,cnt;
  llint now;
  scanf("%d",&tc);
  for(cs=1;cs<=tc;cs++)
  {
    scanf("%d%d",&m,&n);
    for(i=0;i<n;i++)
      scanf("%d",&ary[i]);
    printf("Case #%d: ",cs);
    if(m==1) printf("%d\n",n);
    else
    {
      sort(ary,ary+n);
      ans=n;
      for(i=0;i<=n;i++)
      {
        now=m;
        cnt=i;
        for(j=0;j<n-i;j++)
        {
          if(now>ary[j]) now+=ary[j];
          else
          {
            while(now<=ary[j])
            {
              now+=(now-1);
              ++cnt;
            }
            now+=ary[j];
          }
        }
        if(cnt<ans) ans=cnt;
      }
      printf("%d\n",ans);
    }
  }
  return 0;
}
