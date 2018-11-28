#include<iostream>
#include<string>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        string s;
        int k;
        cin>>s>>k;
        bool filp[1005];
        for(int i=0;i<1005;i++)filp[i]=false;

        int ans=0;

        for(int i=0;i<s.length();i++){
            if(s[i]=='+'&& filp[i]==false){
                continue;
            }

            if(s[i]=='-'&&filp[i]==true){
                continue;
            }

            if(s.length()-i<k){
                ans=-1;
                break;
            }

            ans++;
            for(int j=0;j<k;j++){
                filp[i+j]=!filp[i+j];
            }
        }

        if(ans==-1){
            cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<cas<<": "<<ans<<endl;
        }
    }
}
