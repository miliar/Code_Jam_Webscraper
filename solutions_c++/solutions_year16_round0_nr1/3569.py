#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
   ifstream fin("input.in") ;
   ofstream fout("output.txt") ;
   ll tt ;
   fin>>tt ;
   for(int t = 1;t<=tt;t++)
   {
       fout<<"Case #"<<t<<": ";
       ll n ;
       fin>>n ;
       if(n==0)
       {
           fout<<"INSOMNIA"<<endl ;
           continue ;
       }
       set<ll> ss ;
       ll flag = 0;
       for(ll i = n;i<= 100000*n; i+=n)
       {
           ll k = i ;
           while(k)
           {
               ss.insert(k%10) ;
               k = k/10 ;
           }
           if(ss.size()==10)
           {
               fout<<i<<endl ;
               flag = 1 ;
               break ;
           }
       }
       if(flag==0)
       {
           fout<<"INSOMNIA"<<endl ;
       }
   }
}
