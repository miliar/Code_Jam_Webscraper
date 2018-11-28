#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    int cs = 1;
    while(t--){
        int smax;
        cin>>smax;
        string s;
        cin>>s;
        int cur = 0;
        int ans = 0;
        for(int i=0; i<=smax; i++){
            if(cur <= i){
                ans = ans + (i-cur);
                cur = i;
            }
            cur = cur + s[i]-'0';
        }
        cout<<"Case #"<<cs++<<": "<<ans<<endl;
    }
}
