#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<cstdlib>

typedef long long int lu;

#define MAX 10002

int main()
{
      int t,n,i,j,sum,num;
      char s[MAX];
      freopen("in","r",stdin);
      freopen("out","w",stdout);
      scanf("%d",&t);
      for(i=0;i<t;i++)
      {
            sum=0;num=0;
            scanf("%d%s",&n,s);
            for(j=0;j<=n;j++)
            {
                  if(sum<j)
                  {
                        num+=(j-sum);
                        sum+=(j-sum);
                  }
                  sum+=(s[j]-'0');
                  //printf("%d %d\n",num,sum);
            }
            printf("Case #%d: %d\n",i+1,num);
      }
	return 0;
}
