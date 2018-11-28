#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("C:\\Users\\lenovo\\Downloads\\A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, cas=0;
    cin>>T;
    string s;
    int k;
    while(T--){
        cin>>s>>k;
        int i, ans=0;
        for(i=0; i+k-1<s.length(); ++i){
            if(s[i]=='-'){
                s[i]='+';
                for(int j=i+1; j<i+k; ++j){
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                ++ans;
            }
        }
        string ss(s.length(), '+');
//        cout<<s<<endl;
//        cout<<ss<<endl;
        if(s==ss)
            cout<<"Case #"<<++cas<<": "<<ans<<endl;
        else
            cout<<"Case #"<<++cas<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
