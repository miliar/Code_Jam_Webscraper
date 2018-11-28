#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t,k,l,i;
    cin>>t;
    for(k=1;k<=t;k++){
        string s,ans;
        cin>>s;
        ans=s[0];
        l=s.length();
        for(i=1;i<l;i++){
            if(s[i]>=ans[0]){
                ans=s[i]+ans;
            }
            else{
                ans=ans+s[i];
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
