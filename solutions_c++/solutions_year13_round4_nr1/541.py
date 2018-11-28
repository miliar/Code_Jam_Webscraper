#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <cmath>
#include <iomanip>

#define X first
#define Y second
#define ll long long

using namespace std;


int n, m;
ll base=1000002013;
struct path
{
       int fr, to, p;       
};
vector<path>v;
ll Cost[1010];
ll CC()
{
   ll ans=0;
   for (int i=0; i<v.size(); i++)
   {
       ll A, B, C;
       A=v[i].to-v[i].fr;
       B=v[i].p;
       C=Cost[A]%base*B%base;
       ans+=C;
       ans%=base;
   }       
   return ans;
   
}
void solve(int cas)
{
     //cout<<"--"<<endl;
    // cout<<cas<<endl;
     cin>>n>>m;
     Cost[0]=0;
     for (int i=1; i<=n; i++)
         Cost[i]=Cost[i-1] + n+1-i, Cost[i]%=base;
     v.clear();
     for (int i=1; i<=m; i++)
     {
         int aa, bb, cc;
         scanf("%d%d%d", &aa, &bb, &cc);
         path O; O.fr=aa; O.to=bb; O.p=cc;
         v.push_back(O);    
     }
     ll s1=CC();
     while (1==1)
     {
           //cout<<v.size()<<endl;
           bool fl=0;
           for (int i=0; i<v.size(); i++)
           {
               //cout<<i<<endl;
               
               for (int j=0; j<v.size(); j++)    
               {
                   if ( v[i].p==0 )
                      break;
                   if ( v[i].fr<v[j].fr && v[i].to<v[j].to && v[i].to>=v[j].fr && v[j].p>0 )
                   {
                      fl=1;
                      int zz=min(v[i].p, v[j].p);
                      v[i].p-=zz; v[j].p-=zz;
                      path nw;
                      nw.fr=v[j].fr; nw.to=v[i].to; nw.p=zz;
                      v.push_back(nw);
                      nw.fr=v[i].fr; nw.to=v[j].to; nw.p=zz;
                      v.push_back(nw);     
                   }    
               }
           }      
           if (fl==0)
              break;
     }
     ll s2=CC();
     s1=s1-s2;
     if (s1>=0)
        s1%=base;
     else
        s1=base+s1%base;
     printf("Case #%d: %I64d\n", cas, s1); 
}
int main ()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int test;
    cin>>test;
    for (int i=1; i<=test; i++)
        solve(i);
        
    return 0;    
}
