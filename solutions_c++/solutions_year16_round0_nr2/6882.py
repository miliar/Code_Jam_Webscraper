#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char str[110];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,k=1;
    scanf("%d",&t);
    while(t--)
    {
              int cnt=0;
              scanf("%s",str);
              int i;
              int n=strlen(str);
              for(i=0;i<n;i++)
              {
                 if(str[i]=='-')
                 {
                    if(i==0)
                    cnt++;
                    else
                    cnt+=2;
                    while(str[i]!='+' && i<n)
                    i++;
                 }
          
              }
              printf("Case #%d: %d\n",k,cnt);
              k++;
    }
    return 0;
}
