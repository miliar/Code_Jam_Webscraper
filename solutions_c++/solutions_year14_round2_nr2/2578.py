#include<iostream>
using namespace std;

int main(){
   int t,a,b,k;
   cin>>t;
   int n=1;
   while(t--&&cin>>a>>b>>k){
    int cnt=0;
    for(int i=0;i<a;++i)
     for(int j=0;j<b;++j)
       if((i&j)<k)
         cnt++;
    cout<<"Case #"<<n++<<": "<<cnt<<endl;
   }
}
