#include<bits/stdc++.h>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;++t){
        int n,ans=0;cin >> n;
        string s;
        cin >> s;
        int a[n+10];
        a[0]=s[0]-'0';
        for(int i=1; i <= n+1; ++i){
            ans += max(0,i-a[i-1]);
            a[i-1] += max(0,i-a[i-1]);
            a[i] = a[i-1]+s[i]-'0';
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
