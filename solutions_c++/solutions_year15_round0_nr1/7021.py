#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    int tt,sx;
    string s;
    cin>>tt;
    for(int ttt=1;ttt<=tt;ttt++){
        cin>>sx;
        cin>>s;
       // cout<<sx<<" "<<s<<endl;
        int ans=0,cnt=s[0]-'0';
        for(int i=1;i<=sx;i++){
                if(s[i]=='0')continue;
            if(cnt>=i){
                cnt+=s[i]-'0';
            }else{
               ans+=i-cnt;
               cnt=i;
               cnt+=s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",ttt,ans);
    }
    return 0;
}
