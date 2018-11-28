#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    int a=t;
    while(t--){
                int r, t1;
                cin>>r>>t1;
                double d=4*r*r-4*r+1+8*t1;
                int ans=(int)floor((1-2*r+(double)sqrt(d))/4);
                if(ans<0)
                         ans=0;
                cout<<"Case #"<<a-t<<": "<<ans<<"\n";
               
               
               }    
    
  //  system("pause");
    
    
}
