#include<iostream>
#include<string>
using namespace std;

int main(){
    
    int t=1,T;
    cin>>T;
    while (t<=T){
        int N,ans=0,cc=0;
        string s;
        cin>>N>>s;
        cc = s[0]-'0';
        for (int i=1; i<=N; i++) {
            int cur = s[i]-'0';
            if(cur > 0 && cc<i){
                ans += i - cc;
                cc += i-cc;
            }
            //cout<<ans<<endl;
            cc += cur;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
        t++;
    }
    return 0;
}