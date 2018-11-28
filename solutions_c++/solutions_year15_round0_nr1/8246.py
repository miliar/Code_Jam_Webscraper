#include<iostream>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        int smax,ans=0,aud=0;
        string str;
        cin>>smax>>str;
        for(int j=0;j<=smax;j++){
            if((str[j]-'0')!=0 && aud<j){
                ans+=j-aud;
                aud=j;
            }
            aud+=str[j]-'0';
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
