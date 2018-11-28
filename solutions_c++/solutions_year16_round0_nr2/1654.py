#include <bits/stdc++.h>

using namespace std;

string s;

void clearmem(){
}

void solve(){
    clearmem();
    cin >> s;
    s += '+';
    int ls = s.size(),csum = 0,ans = 0;
    bool chk = false;
    char st;
    string ts;
        chk = true;
        st = s[0];
        for (int i=1;i<ls;i++){
            if (st!=s[i]){
                for (int j=i-1;j>=0;j--)
                    s[j] = s[i];
                st = s[i];
                ans++;
            }
        }
    printf ("%d\n",ans);
}

int main(){
    freopen ("B-large.in","r",stdin);
    freopen ("Blarge.out","w",stdout);
    int TC;
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }
return 0;
}
