#include <iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<string.h>
#include<sstream>
#include<algorithm>
using namespace std;

int main()
{
          int t,n;
          char a[1001],b;
          scanf("%d",&t);
          for(int j=1;j<=t;j++)
          {
              scanf("%d",&n);
              getchar();
              int count=0,l,total=0,num;
              for(int i=0;i<(n+1);i++)
              {
                  scanf(" %c",&b);
                  l=b-'0';
                 if(l==0&&i==0)
                 {
                     total++;
                     count++;
                 }
                 else if(l==0&&(i+1)>total)
                 {
                     total++;
                     count++;
                 }
                 else
                 {
                     total+=l;
                 }
              }
              printf("Case #%d: %d\n",j,count);
          }
    return 0;
}
