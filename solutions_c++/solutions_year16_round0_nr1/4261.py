#include<iostream>
#include<algorithm>
#include<set>
#define REP(i,n) for(int i=0;i<n;++i)
using namespace std;

void solve(long long n){
   set<long long> d;
   set<long long> v;
   
   if(n==0)
   {
           cout<<"INSOMNIA"<<endl;
           return;
   }
   long long j = 1;
   
   while(true)
   {
      long long l = j*n;
      if(v.find(l)!=v.end()) 
      { cout<<"INSOMNIA"<<endl; break;}
      v.insert(l);
      
      while(l>0)
      {
         long long dg = l%10;
         d.insert(dg);
         l/=10;
      }
      

      if(d.size()==10)
       {
         cout<<(j*n)<<endl;
         break;
       }
             ++j;
   }
}


int main(){
    int t; cin>>t;
    REP(j,t) 
    {
             int u;cin>>u;
             cout<<"Case #"<<(j+1)<<": ";
             solve((long long)u);
             }
    return 0;   
}
