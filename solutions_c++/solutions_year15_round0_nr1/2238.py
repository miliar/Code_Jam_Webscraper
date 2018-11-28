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
string s;
int n, m, k, i, j, t, res, cur;
main(){
       freopen("A.in","r",stdin);
       freopen("A.out","w",stdout);
       cin>>t;
       for(int I=1;I<=t;I++)
        {
         cin>>n;
         cin>>s;
         cur=s[0]-'0'; res=0;
         for(i=1;i<=n;i++)
          {
          // cout<<cur<<" "<<i<<endl;
           if(cur>=i)cur+=(s[i]-'0');
           else res+=i-cur, cur+=i-cur+(s[i]-'0');
          }
         cout<<"Case #"<<I<<": "<<res<<endl;
        } 
       }
