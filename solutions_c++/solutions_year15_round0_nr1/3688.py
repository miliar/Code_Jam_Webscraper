#include <iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int teste,ad,sum,smax;
char sir[2000];
int main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
cin>>teste;
for(int i=1; i<=teste; i++)
{
    ad=0;
    sum=0;
    cin>>smax;
    cin>>sir;

    sum=sir[0]-'0';
    for(int j=1; j<=smax; j++)
    {
      if(sir[j]>'0')
      {
          if(sum>=j)sum=sum+sir[j]-'0';
          else {
            ad=ad+j-sum;
            sum=j;
            sum=sum+sir[j]-'0';

          }


      }
    }
printf("Case #%d: %d\n",i,ad);
}

    return 0;
}
