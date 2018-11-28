#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int T;
char s[120];
int main()
{
  int t,i,l,ans;
  FILE *f;
  f=fopen("/Users/Basun/Documents/programming/Google Code Jam 2016/A/B Revenge of the Pancakes/in.txt", "r");
  fscanf(f,"%d",&T);
  for(t=0;t<T;t++)
  {
    fscanf(f,"%s",s);
    l=(int)strlen(s);
    ans=0;
    for(i=0;i<l;i++)
    {
      if (i==0&&s[i]=='-')
        ans+=1;
      else if (i>0&&s[i]=='-'&&s[i-1]=='+')
        ans+=2;
    }
    printf("Case #%d: %d\n",t+1,ans);
  }
  return 0;
}
