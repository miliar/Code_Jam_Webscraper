#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main(){
   freopen("input.txt","r",stdin);
   freopen("output1.out","w",stdout);
   int cs,idx =0;
   cin>>cs;

   while(cs--){
      int s,nf =0,ps =0;
      string cad;
      cin>>s>>cad;

      for(int i=0; i<s+1; i++){
         if(i > ps && (cad[i]-'0')){
            nf+= (i - ps);
            ps+= (i - ps);
         }
         ps+= (cad[i]-'0');
      }

      cout<<"Case #"<<++idx<<": "<<nf<<endl;
   }
}
