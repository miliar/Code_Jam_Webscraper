#include<iostream>
#include<string>
using namespace std;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        string in;
        char now;
        int ans=0;
        cin>>in;
        now=in[0];
        for(int i=1;i<in.length();i++){
            if(in[i]!=now){
                ans++;
                now=in[i];
            }
        }
        if(now!='+')ans++;
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
}

