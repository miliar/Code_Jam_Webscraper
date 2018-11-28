#include<stdio.h>
#include<string.h>
#define ri(x) scanf("%d",&(x))
#define rep(x,y) for(int x=1;x<y;x++)
int main()
{
 int tk,tk1=0;
 ri(tk);
 while (tk--)
 {
  tk1++;
  printf("Case #%d: ",tk1);
  int ans=0,n1,n2;
  int f[20]={0};
  ri(n1);
  rep(i,5)
   rep(j,5)
   {
    int x;
    ri(x);
    if(n1==i)f[x]=1;
   }
  ri(n2);
  rep(i,5)
   rep(j,5)
   {
    int x;
    ri(x);
    if (f[x] && i==n2)
    {
     if(ans)
      ans=-1;
     else ans=x;
    }
   }
  if(ans==-1)
     printf("Bad magician!\n");
  if(ans==0)
     printf("Volunteer cheated!\n");
  if(ans>0)
     printf("%d\n",ans);
 }
}
