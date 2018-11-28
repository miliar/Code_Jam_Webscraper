#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define UP upper_bound
#define LB lower_bound
#define LL long long 
#define Pi 3.14159265358
#define si size()
#define en end()
#define be begin()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii set<int>::iterator i
#define is set<string>::iterator i
using namespace std;
double res, ans, ans1, C, F, X, paa, cur;
int i, t;
main(){
       freopen("B.in","r",stdin);
       freopen("B.out","w",stdout);
       cin>>t;
       for(i=1;i<=t;i++)
        {
         paa=0.0;
         ans=0.0;
         cur=2.0;
         ans1=0.0;
         res=100000000.00000;
         cin>>C>>F>>X;
         while(true)
          {
           ans=paa;
           ans+=X/cur;
          // cout<<ans<<" ";
           if(ans>ans1 && ans1)break;
           ans1=ans;
           res=MIN(ans,res);
           paa+=C/cur;
           cur+=F;
          }
         cout<<"Case #"<<i<<": ";
         printf("%.7f\n",res);
        }
       //system("pause");
       }
