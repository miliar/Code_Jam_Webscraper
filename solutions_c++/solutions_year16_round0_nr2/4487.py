#include <iostream>

using namespace std;

int main(){
    int t,n,cnt,i;
    cin>>t;
    for (int x=1;x<=t;x++){
        int ans=0;
        string s;
        cin>>s;
        n = s.size();
        cnt=0;
        i=0;
        while (i<n){
            if (s[i]=='+'){
                i++;
                while (s[i]=='+' && i<n){
                    i++;
                }
            }
            else{
                cnt++;
                while (s[i]=='-' && i<n){
                    i++;
                }
            }
        }
        if (s[0]=='+'){
            ans = cnt*2;
        }
        else{
            ans = 2*cnt - 1;
        }
        cout<<"Case #"<<x<<": "<<ans<<"\n";
    }
}
