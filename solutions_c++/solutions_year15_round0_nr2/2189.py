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
#define ii set<int>::iterator
#define Tree int ind, int L, int R
#define Left 2*ind,L,(L+R)/2
#define Right 2*ind+1,(L+R)/2+1,R
using namespace std;
int a[1001];
int b[1001];
int x[1001];
int n, m, k, i, j, t, res, cnt;
main(){
       freopen("B.in","r",stdin);
       freopen("B.out","w",stdout);
       cin>>t;
       for(int I=1;I<=t;I++)
        {
         cin>>n;
         res=1000000000;
         memset(x,0,sizeof(x));
         for(i=1;i<=n;i++)
          {
           cin>>a[i];
           x[a[i]]++;
          }
         for(i=1;i<=1000;i++)
          {
           cnt=0;
           for(j=1;j<=1000;j++)b[j]=x[j];
           for(j=1000;j>i;j--)
            {
             cnt+=b[j];
             b[j-i]+=b[j];
             b[i]+=b[j];
            }
           for(j=i;j>=1;j--)
             if(b[j]!=0)
              { cnt+=j; break; }
           res=min(res,cnt);
          }
         cout<<"Case #"<<I<<": "<<res<<endl;
        }
       cin>>n;
       }
