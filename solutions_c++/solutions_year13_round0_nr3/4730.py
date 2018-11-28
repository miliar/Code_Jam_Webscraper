#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
    //freopen("C:\\Users\\DELL\\Desktop\\input.txt","r",stdin); 
//freopen("C:\\Users\\DELL\\Desktop\\output.txt","w",stdout);
     long long int a1[39]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
     long long int t,a,b,pro,t1,i,count;
     scanf("%lld",&t);
     for(t1=1;t1<=t;t1++)
     {
               scanf("%lld %lld",&a,&b);
               count=0;
               for(i=0;i<39;i++)
               {
               pro=a1[i]*a1[i];
               if(a<=pro&&pro<=b)
               count++;
               }
               printf("Case #%lld: %lld\n",t1,count);
               }
               return 0;
               }
