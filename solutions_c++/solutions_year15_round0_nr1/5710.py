#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("mylargefile.txt","w",stdout);
    int t;
    cin>>t;
    for(int h=1;h<=t;h++){
        int length;
        cin>>length;
        string s;
        cin>>s;
        long long int ans=0,cu=0;
        for(int i=0;i<=length;i++){
            if(cu<i){
                ans+=i-cu;
                cu+=i-cu;
            }
            cu+=s[i]-48;
        }
        cout<<"Case #"<<h<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
