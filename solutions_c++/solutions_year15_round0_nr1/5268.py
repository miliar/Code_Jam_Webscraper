#include<iostream>
#include<string>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TC;
    cin>>TC;
    for(int ZZ=1;ZZ<=TC;ZZ++){
        int l;
        cin>>l;
        string s;
        cin>>s;
        int ok = 0;
    int ans = 0;
        for(int i=0;i<s.length();i++){
            if(ok<i){
                ans+=i-ok;
                ok+=i-ok;
            }
            ok+=s[i] - '0';
            if(ok>=l)
                break;
        }
        cout<<"Case #"<<ZZ<<": "<<ans<<endl;
    }
    return 0;
}
