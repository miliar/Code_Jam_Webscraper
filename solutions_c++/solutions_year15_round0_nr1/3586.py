#include<bits/stdc++.h>
using namespace std;
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-largeOut.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int z=1; z<=t; z++) {
        int n;
        string s;
        cin>>n>>s;
        int x=s[0]-'0',ans=0;
        for(int i=1; i<=n; i++) {
            int y=s[i]-'0';
            if(s[i]>'0') {
                if(x<i) {
                    int a=i-x;
                    ans+=a;
                    x+=a;
                    x+=y;
                } else {
                    x+=y;
                }
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
