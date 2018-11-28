#include <iostream>
using namespace std;

int main(){
     int t,tc,n,i,ans,counter,num;
     string s;
     cin>>t;
     tc=1;
     while(t--){
        cin>>n;
        ans=0;
        counter=0;
        num=0;
        cin>>s;
        for(i=0;i<=n;i++){
            if(i>0) num = s[i-1] - '0';
            counter+=num;
            if(i > counter && s[i]!='0'){
                ans+=i-counter;
                counter+=ans;
            }
        }
        cout<<"Case #"<<tc<<": "<<ans<<endl;
        tc++;
     }
}
