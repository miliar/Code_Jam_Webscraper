#include<iostream>
#include<vector>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        string s;
        cin>>s;
        string ans="";
        for(auto x:s)
            if(ans==""||ans[0]>x)
                ans += x;
            else
                ans = x + ans;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
