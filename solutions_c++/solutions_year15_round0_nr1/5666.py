#include<stdio.h>
char s[10001];
int main()
{
    freopen ("out1.txt","w",stdout);
    freopen ("A-large.in","r",stdin);
    int t,smax,cas=0;
    scanf("%d",&t);
    while(cas++<t)
    {
          scanf("%d%s",&smax,s);
          //printf("%d %s\n",smax,s);
          int ans = 0;
          int standing = 0, i = 0;
          while(s[i])
          {
              int c = s[i]-'0';
              if( standing >= i )
                    standing+=c;
              else if(c>0)
              {
                   ans += i-standing;
                   standing+=i-standing;
                   standing+=c;
              }
              if(standing>=smax)break;
              
             // printf("i=%d: ans=%d %d\n",i,ans,standing);
              i++;
          }
          printf("Case #%d: %d\n",cas,ans);
    }
    
    return 0;  
}
