#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int palin(int n)
{
    char str[100], copy[100];
    sprintf(str,"%d",n);
    strcpy(copy, str);
    string strdup(str);
    reverse(strdup.begin(), strdup.end());
    const char* str1 = strdup.c_str();
    if( !strcmp(str1, copy)) return 1;
    return 0;
}

int fns(int n)
{
    if (!palin(n) ) return 0;
    int root = sqrt(n);
    if(root*root != n) return 0;
    
    if( !palin(root) ) return 0;
    return 1;
}

main()
{
      int arr[1200] = {0}, ans[1200];
      for(int i=1; i<=1000; i++)
      {
          if(fns(i))
          arr[i] = 1;
      }
      ans[0] = 0;
      ans[1] = 1;
      for(int i=2; i<=1000; i++)
      if(arr[i])
      ans[i] = ans[i-1]+1;
      else
      ans[i] = ans[i-1];
      int tc,t, a, b;
      scanf("%d",&tc);
      for(t=1; t<=tc; t++)
      {
          scanf("%d%d", &a, &b);
          cout<<"Case #"<<t<<": "<<ans[b]-ans[a-1]<<endl;
      }
}
