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

ll n, p, s=1;

ll canmx(ll S, ll x)
{
   //cout<<S<<" "<<x<<endl;         
   if ( x==0 )
      return 0;
   ll res=S/2;
   if ( x%2==0 )
      return res+canmx(S/2, x/2-1);
   else
      return res+canmx(S/2, x/2);       
}
ll bin(ll st, ll fin, ll P)
{
   //cout<<st<<" "<<fin<<" "<<P<<endl;
   if (st==fin)
      return st;
   ll med=(st+fin+1)/2; 
   if ( canmx(s, med)>P )
      return bin(st, med-1, P);
   else
      return bin(med, fin, P);          
}

ll bin2(ll st, ll fin, ll P)
{
   // cout<<st<<" "<<fin<<" "<<P<<endl;
   if (st==fin)
      return st;
   ll med=(st+fin+1)/2;
   if ( s-1-canmx(s, s-1-med)>P )
      return bin2(st, med-1, P);
   else
      return bin2(med, fin, P);           
}
void solve(int cas)
{
     cin>>n>>p;
     p--;
     s=1;
     for (int i=1; i<=n; i++)
         s=s+s;
     //cout<<s<<endl;
     ll ans1=bin(0, s-1, p);  
     ll ans2=bin2(0, s-1, p);
     //ans2=s-1-ans2;
     printf("Case #%d: %I64d %I64d\n", cas, ans1, ans2);
}
int main ()
{
    //cout<<canmx(8, 0);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test;
    cin>>test;
    for (int i=1; i<=test; i++)
        solve(i);
    return 0;    
}
