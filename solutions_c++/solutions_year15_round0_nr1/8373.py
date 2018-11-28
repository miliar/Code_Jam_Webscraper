#include<cstdio>
#include<iostream>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>> t;
    int cases = 0;
    while (t--){
        cases++;
        int cnt;
        cin>>cnt;
        string s;
        cin>>s;
        int ans = 0;
        for (int i=1;i<s.size();i++){
            int tmp=0;
            for (int j=0;j<i;j++)
                tmp+=s[j]-'0';
            ans=max(ans,i-tmp);
        }
        cout<<"Case #"<<cases<<": "<<ans<<endl;
    }
}
