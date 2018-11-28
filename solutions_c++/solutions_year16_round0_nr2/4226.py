#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("INP.txt","r+",stdin);
    freopen("ANS.txt","w+",stdout);
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        string str;
        cin>>str;
        int ans=0;
        for(int j=0;j<str.length();){
            while(j+1<str.length() && str[j+1]==str[j])j++;
            if(j==str.length()-1 && str[j]=='-'){
                ans++;
                break;
            }
            else if(j==str.length()-1 && str[j]=='+') break;
            else ans++,j++;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
