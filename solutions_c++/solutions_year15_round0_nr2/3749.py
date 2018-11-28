#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
#define maxn 10
#define inf 100000000
int T;
int n;
int s[maxn];
int main()
{
   freopen("D:/B-large.in","r",stdin);
   freopen("G:/out.txt","w",stdout);
   cin>>T;
   int case_=0;
     while(T--)
       {
           int mm=0,ans=inf;
           scanf("%d",&n);
           for(int i=0;i<n;i++)
            scanf("%d",&s[i]);
            for(int i=0;i<n;i++)
                mm=max(mm,s[i]);
           for(int i=1;i<=mm;i++)
           {
               int ant=0;
               for(int j=0;j<n;j++)
               {
                   int pp=s[j]/i;
                   if(s[j]%i==0 && pp)
                    pp--;
                   ant+=pp;
               }
               ans=min(ans,ant+i);
           }
           printf("Case #%d: %d\n",++case_,ans);
       }
       return 0;
   }
