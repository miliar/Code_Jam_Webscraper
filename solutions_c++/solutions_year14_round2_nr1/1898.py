#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char str[4][105];
int main()
{

freopen("A-small-attempt0.in","r",stdin);
freopen("output","w",stdout);
int freq[20];
int t,N,a,b,total,l1,l2,f,d,c;
scanf("%d",&t);
for(a=1;a<=t;a++)
{
  total = 0;
  f = 1;
  scanf("%d",&N);
  for(b=1;b<=N;b++)
  scanf("%s",str[b]);

  l1 = strlen(str[1]);
  l2 = strlen(str[2]);
  d=1;
  //for(d=1;d<N;d++)
 // {
  for(b=0,c=0;b<l1 || c<l2;)
  {
    if(b<l1 && c<l2 && str[d][b]==str[d+1][c])
    {
      b++;
      c++;
    }
    else if(b!=0 && str[d][b-1]==str[d][b])
    {
      total++;
      b++;
    }
    else if(c!=0 && str[d+1][c-1]==str[d+1][c])
    {
      c++;
      total++;
    }
    else
    {
      printf("Case #%d: Fegla Won\n",a);
      f = 0;
      break;

    }
  }
  if(f==1)
  printf("Case #%d: %d\n",a,total);
 // }

}
return 0;
}
