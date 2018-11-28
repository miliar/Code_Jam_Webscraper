#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define s(n) scanf(" %d",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf("%d %d",&a,&b)
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define ii pair<int,int>
#define F first
#define S second
#define P printf
#define E <<endl
#define mid (st+(end-st)/2)
using namespace std;
int t,d,i,j,maxm,ans,sum,cnt;
float ar[1004];
int main()
{
   freopen("B-large.in","r",stdin);
   freopen("op2.txt","w",stdout);
   s(t);
   cnt=0;
   while(t--)
   {
      s(d);
      maxm=0;
      cnt++;
      for(i=1;i<=d;i++)
      {
          scanf("%f",&ar[i]);
          if(ar[i]>maxm)
          maxm=ar[i];
      }
      ans=maxm;
      for(i=1;i<=maxm;i++)
      {
          sum=i;
          for(j=1;j<=d;j++)
          {
          	//int tmp=ceil(ar[j]/i)-1;
          	//cout<<"tmp"<<tmp;
             sum+=(ceil(ar[j]/i)-1);
          }
         // cout<<"sum"<<sum;
          ans=min(sum,ans);
      }
      P("Case #%d: %d\n",cnt,ans);
   }
   return 0;
}
