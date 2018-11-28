#include<iostream>
#include<string.h>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<cstdio>
using namespace std;
char ch;

int main()
{
  int p,q,t,ans;char c;
  double f;
  bool a;
  ifstream fin;
  ofstream fot;
  freopen("gg.in","r",stdin);
  freopen("ans.out","w",stdout);
  scanf("%d",&t);
  for(int i=0;i<t;i++)
  {
      scanf("%d%c%d",&p,&c,&q);ans=0;f=double(p)/double(q);a=true;
      while(q>1)
      {
        if(q%2==0)
         q=q/2;
         else
          {
          a=false;
          break;
          }
      }
      if(a)
      {
    while(f<1)
      {
       f*=2;
       ans++;
      }
      if(ans<41)
           printf("Case #%d: %d\n",i+1,ans);
      else
          printf("Case #%d: impossible\n",i+1);
      }
      else
           printf("Case #%d: impossible\n",i+1);
  }
return 0;
}
