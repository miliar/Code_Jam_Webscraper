#include<bits/stdc++.h>
using namespace::std;
void solve(string s,int k){
    int cnt = 0;
    bool bad = false;
    bool ok = true;
    while(ok){
        ok = false;
        int i=0;
        while(i<s.size()){
            int st = -1;
            if(s[i]=='-'){
                if(i+k-1 >= s.size()){ bad = true; break; }
                for(int j=1;j<=k;j++){
                    if(s[i]=='-') s[i]='+';
                    else {
                        s[i]='-';
                        if(st == -1) st = i;
                    }
                    i++;
                }
                cnt++;
                if(st!=-1) i = st;
            }
            else{
                i++;
            }
            if(bad) break;
        }
        //cout << s << " " << bad << endl;
        if(bad) break;

        for(int i=0;i<s.size();i++){
            if(s[i]=='-') ok = true;
        }
    }
    if(bad) cout << "IMPOSSIBLE" << endl;
    else cout << cnt << endl;
}
int main(){
    int T,k;
    string s;
    cin >> T;
    for(int tt=1;tt<=T;tt++){
        cin >> s >> k;
        printf("Case #%d: ",tt);
        solve(s,k);
    }
}
