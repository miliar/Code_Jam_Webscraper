#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    int t,c=1;
    cin>>t;
    while(t--) {
               int s,count=0,sum=0,curr;
               cin>>s;
               for(int i=0;i<=s;i++){
                       scanf("%1d",&curr);
                       if (count<i){
                          sum+=i-count;
                          count+=i-count;
                       }
                       count+=curr;
               }
               cout<<"Case #"<<c++<<": "<<sum<<endl;
    }
    return 0;
}
