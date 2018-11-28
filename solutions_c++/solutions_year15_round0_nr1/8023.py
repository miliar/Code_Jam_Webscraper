#include <stdio.h>
#include <string.h>
int main()
{
  //freopen("in.txt","r",stdin);
  //freopen("out.txt_1_large","w",stdout);
  int i,j,t,p[1002],s,ans;
  char ch[1002];
  scanf("%d",&t);
  for(i=0;i<t;i++)
  {
    ans=0;
    memset(p,0,sizeof(p));
    scanf("%d",&s);
    scanf("%s",ch);
    if(ch[0]-48>0)
      p[0]=ch[0]-48;
    else
      p[0]=1,ans++;
    for(j=1;j<=s;j++)
    {
      if(p[j-1]<j)
      {
        ans+=j-p[j-1];
        p[j-1]=j;
      }
      p[j]+=p[j-1]+ch[j]-48;
    }
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}
