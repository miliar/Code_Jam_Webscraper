#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    freopen("ooo.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>T;
    int cases=0;
    while(T--){
        cases++;
        int ans=0;
        string s;
        cin>>s;
        for(int i=1;i<s.size();i++){
            if(s[i]=='-'&&s[i-1]=='+')ans+=2;
        }
        if(s[0]=='-')ans++;
        cout<<"Case #"<<cases<<": "<<ans<<"\n";
    }
    return 0;
}
