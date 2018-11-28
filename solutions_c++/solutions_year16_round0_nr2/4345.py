#include<iostream>
#include<algorithm>
#include<set>
#include<string>
#include<vector>
#define REP(i,n) for(int i=0;i<n;++i)
using namespace std;

int solve(string input){
  int ret = 0;
  
  vector<int> v(input.size(),0);
  REP(i,input.size()) if(input[i]=='+') v[i]=1;
  //REP(i,v.size()) cout<<v[i]<<" ";cout<<endl;
  int i = input.size()-1;
  while(i>=0)
  {
          
          if(v[i]==0)
          {
                     ++ret;
                     if(v[0]==0)
                     {
                         for(int j=0;j<=(i/2);++j)
                         swap(v[j],v[i-j]);
                         for(int j=0;j<=i;++j)
                          if(v[j]==0) v[j]=1;
                          else v[j]=0;
                        //reverse range
                     }
                     else 
                     {
                          int r = 0;
                          while(v[r+1]==1) ++r;
                           for(int j=0;j<=(r/2);++j)
                         swap(v[j],v[r-j]);
                         for(int j=0;j<=r;++j)
                          if(v[j]==0) v[j]=1;
                          else v[j]=0;
                          
                     }

          }
          else --i;
         // REP(i,v.size()) cout<<v[i]<<" ";cout<<endl;
  }
  
  return ret;
}


int main(){
    int t; cin>>t;
    REP(j,t) 
    {
             string u;cin>>u;
             int ret = solve(u);
              cout<<"Case #"<<(j+1)<<": "<<ret<<endl;
             }
    return 0;   
}
