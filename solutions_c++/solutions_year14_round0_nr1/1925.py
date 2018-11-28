#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{

freopen("A-small-attempt0.in","r",stdin);
freopen("output","w",stdout);
int freq[20];
int t , a , b , c , row,col,card,tw,ans;
scanf("%d",&t);
for(a=1;a<=t;a++)
{
  memset(freq,0,sizeof(freq));
  scanf("%d",&row);
  for(b=1;b<=4;b++)
  for(c=1;c<=4;c++)
  {
     scanf("%d",&card);
     if(b==row)
     freq[card]++ ;
  }
  scanf("%d",&row);
  for(b=1;b<=4;b++)
  for(c=1;c<=4;c++)
  {
     scanf("%d",&card);
     if(b==row)
     freq[card]++ ;
  }
  tw = 0;
  for(b=1;b<=16;b++)
  {
    if(freq[b]==2)
    {
    tw++;
    ans = b;
    }
  }
  if(tw==1)
  printf("Case #%d: %d\n",a,ans);
  else if(tw>1)
  printf("Case #%d: Bad magician!\n",a);
  else
  printf("Case #%d: Volunteer cheated!\n",a);

}
return 0;
}
