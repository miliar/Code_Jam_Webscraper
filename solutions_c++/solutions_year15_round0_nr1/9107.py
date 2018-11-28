#include<bits/stdc++.h>
#include <string> 
using namespace std;

main(){
  int t,x,min=0,sum=0;
  string g;
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>x; 
    cin>>g;
         if((g[0]-'0')==0){
           min++;
           sum++;
         }

    for(int j=0;j<g.length()-1;j++){
      sum=sum+(g[j]-'0');
      if(sum>=j+1){}
      else{ 
      while(sum<j+1){
        min++;
        sum++;
        }
      }
    } 
    cout<<"Case #"<<i+1<<": "<<min<<"\n";
    sum=0;min=0;
  }
}
