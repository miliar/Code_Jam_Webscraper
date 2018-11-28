#include<bits/stdc++.h>
using  namespace std;

int main(){
    freopen("A.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,tc= 1;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        n++;
        string s;
        cin>>s;
        int ans = 0;
        int r = 0; // bo8jih
        for(int i=0;i<n;i++){

            int need = i;
            if(!(s[i]-'0')) continue;
            if(r<need){
                ans+=need-r;
                r+=need-r;
            }
            r+=s[i]-'0';
        }
        printf("Case #%d: %d\n",tc++,ans);
    }
    return 0;
}
