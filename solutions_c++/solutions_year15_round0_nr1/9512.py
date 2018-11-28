// b@ver
#include<cstdio>
#include<iostream>
#include<algorithm>
#include <cmath>
#include <vector>
#include<queue>
#include<stack>
#include<map>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<climits>
#define LL long long int
#define inf 2000000000
#define MAX 1002
using namespace std;
int sum[MAX]={0};
int main()
{
  // freopen("input.txt","r",stdin);
   int t,temp;
   cin>>t;
   temp=t;
   while(t--){
   int smax;
   cin>>smax;
   string s;
   cin>>s;
   //cout<<"s was "<<s<<endl;
   int ans=0,i;
   sum[0]=s[0]-'0';
   for(i=1;i<(int)s.length();i++)
   {
      if((s[i]-'0')>0)
      {
        // cout<<" i'm here bitch"<<endl;
         //cout<<" sum of i-q has "<<sum[i-1]<<endl;
         if(sum[i-1]<i)
         {
           // cout<<"i'm now here too"<<endl;
            ans+=(i-sum[i-1]);
         //   cout<<"ans ="<<endl;
            sum[i-1]+=(i-sum[i-1]);
            sum[i]=sum[i-1]+(s[i]-'0');
         }
         else
            sum[i]=sum[i-1]+(s[i]-'0');
      }
      else
         sum[i]=sum[i-1]+(s[i]-'0');
   }
   cout<<"Case #"<<temp-t<<": "<<ans<<endl;
   }
   fclose(stdin);
   return 0;

}


