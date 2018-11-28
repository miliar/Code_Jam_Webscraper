#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    int test;
    cin>>test;
    for(int i=1;i<=test;i++){
        string s;
        cin>>s;
        int ans=0;

        for(int j=0;j<s.length();){
            while(j+1<s.length() && s[j+1]==s[j])j++;
            if(j==s.length()-1){
                if(s[j]=='-')ans++;
                    break;
            }
            else ans++,j++;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;

    }
    return 0;
}
