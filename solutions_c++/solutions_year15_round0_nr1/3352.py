#include<iostream>
#include<cstdio>
#include<memory.h>
#include<algorithm>
#include<math.h>
#define s(n) scanf("%d",&n)
using namespace std;
#define lint unsigned long long int
#define mod 1000000007
int main()
{
 freopen("A-large.in","r",stdin);
   freopen("outputl.txt","w",stdout);
 int t,s;
 s(t);
 for(int j=1;j<=t;j++)
 {
     s(s);
     int ans=0,pos=0;
     char arr[s+2];
     scanf("%s",arr);
     for(int i=0;i<s+1;i++)
     {
         //cin>>arr[i];
         if(arr[i]-'0'>0)
         pos=pos+arr[i]-'0';
         else
         {
             ans=max(ans,(i+1-pos));
         }
     }
     printf("Case #%d: %d\n",j,ans);
 }
 return 0;
 }
