#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm> 
#include<string.h>
#include<map>
using namespace std;
long long miao[50]=
{
1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,
100020001,102030201,104060401,121242121,123454321,125686521,400080004,
404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,
1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,
1024348434201ll,1210024200121ll,1212225222121ll,
1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll

};
int main()
{
freopen("3.in","r",stdin);
freopen("3.out","w",stdout); 
int test;
cin>>test;
long long a,b;
int cas=1;
while(test--)
{
  cin>>a>>b;
  int sum=0;/*
  for(int i=0;i<40;i++)
  cout<<miao[i]<<endl;
  system("pause");*/
  for(int i=0;i<40;i++)
   {
     if(miao[i]<a)continue;
     if(miao[i]>b)break;
     if(miao[i]>=a && miao[i]<=b)
         {
            sum++;       
         }    
   } 
   printf("Case #%d: %d\n",cas++,sum);             
}
//system("pause");
return 0;} 
