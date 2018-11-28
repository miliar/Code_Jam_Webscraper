#include <iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
int teste,d,sec,minim;
int p[1100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
 cin>>teste;
 for(int i=1; i<=teste; i++)
 {
cin>>d;
for(int j=1; j<=d; j++)cin>>p[j];
sec=0;
minim=1000000000;
for(int k=1; k<=1000; k++)
{
sec=0;
   for(int j=1; j<=d; j++)
   {
       if(p[j]>k)
       {
           int dif=p[j]-k;
           if(dif%k==0)sec=sec+dif/k;
           else sec=sec+dif/k+1;
       }
   }
    if(sec+k <minim)minim=sec+k;
}
printf("Case #%d: %d\n",i,minim);
 }

    return 0;
}
