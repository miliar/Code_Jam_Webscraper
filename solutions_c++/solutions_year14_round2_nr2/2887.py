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
  int a,b,k,t,ans;
  ifstream fin;
  ofstream fot;
  freopen("gg.in","r",stdin);
  freopen("ans.out","w",stdout);
  scanf("%d",&t);
  for(int i=0;i<t;i++)
  {
      scanf("%d%d%d",&a,&b,&k);ans=0;
      for(int j=0;j<a;j++)
      {
        for(int l=0;l<b;l++)
       {
          if((j&l)<k)
            ans++;
       }
      }
      printf("Case #%d: %d\n",i+1,ans);
  }
return 0;
}
