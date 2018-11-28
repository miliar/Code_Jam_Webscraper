#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#define LENGTH 1000005
using namespace std;

int main()
{
   //freopen("C:\\input\\A-large.in","r",stdin);
   //freopen("C:\\input\\output.out","w",stdout);
   int T;
   int Case=1;
   scanf("%d",&T);
   while (T--)
   {
       int mx=0;
       string s;
       cin>>mx;
       cin>>s;
       int length=s.length();
       int sum=s[0]-'0';
       int cnt=0;
       int tmp;
       for (int i=1;i<length;i++)
       {
           tmp=s[i]-'0';
           if (tmp)
           {
               if (sum>=i)
                sum+=tmp;
               else
               {
                   cnt+=i-sum;
                   sum=i+tmp;
               }
           }
       }
       cout<<"Case #"<<Case++<<":"<<" "<<cnt<<endl;
   }
   return 0;
}
