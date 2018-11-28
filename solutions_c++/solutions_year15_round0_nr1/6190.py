#include<bits/stdc++.h>
using namespace std;
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        int smax;
        string s;
        cin>>smax;
        cin>>s;
        int count=0;
        int tc=0;
        for(int j=0;j<=smax;j++){
            if((s[j]-'0') and j>tc) {
                count+=(j-tc);
                tc+=(j-tc);
            }
            tc+=(s[j]-'0');
            //cout<<"Current tc at "<<j<<" = "<<tc<<endl;
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}