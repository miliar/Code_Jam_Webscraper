#include<bits/stdc++.h>
using namespace std;
int main()
{

    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
        long long  n;string str;
        cin>>n>>str;
        long long  ans=0,sum=0;
        if(str[0]=='0'){ans++;str[0]='1';}
        for(int i=1;i<str.length();i++){
                sum+=(str[i-1]-'0');
            if(str[i]=='0'&&sum<i+1){
                str[i]='1';ans++;
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
