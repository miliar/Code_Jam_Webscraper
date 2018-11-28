#include <bits/stdc++.h>

//Team UzhNU_MagicalPony
//Author Egor Bobyk

using namespace std;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    //freopen("quant.in","r",stdin);
    //freopen("quant.out","w",stdout);

    int tests;
    cin>>tests;
    int t = 0;
    while (tests--){
        string s;
        cin>>s;
        t++;
        int n = s.size();
        int ans = 0;
        cout<<"Case #"<<t<<": ";
        for (int i = 0; i < n; i++){
            if (i && s[i] != s[i-1]){
                ans++;
            }
        }
        if (s[n-1] == '-') ans++;
        cout<<ans<<endl;
    }
}
