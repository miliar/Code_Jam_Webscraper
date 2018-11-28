#include <bits/stdc++.h>
#include <fstream>
using namespace std;
typedef long long int LL;
int main()
{
    
    long long int t;
    cin>>t;

   for(int i=1;i<=t;i++){
        string s;
        cin>>s;
        LL len = s.length();
        LL ans=0;
        //cout<<s;
        if(s[0]=='-'){
            for(int i=0;i<len-1;i++){
                if(s[i]=='+' && s[i+1]=='-'){
                    ans+=2;
                }
            }
            ans++;
        }
        else{
            for(int i=0;i<len-1;i++){
                if(s[i]=='+' && s[i+1]=='-'){
                    ans+=2;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    return 0;
}