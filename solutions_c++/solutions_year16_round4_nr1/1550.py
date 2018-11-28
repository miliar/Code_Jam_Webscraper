#include <bits/stdc++.h>

using namespace std;

int n, r, p, s;
string str[3];
int cnt[3];

bool solve() {
    /*
    PS
    PRPS
    PRRSPRPS

    PS
    PSPR
    PRPSPRRS
    */
    str[0] = "PR"; str[2] = "PS"; str[1] = "RS";
    string ans = "";
    for(int i = 0;i < 3; i++) {
        vector<int> vt, tmp;
        vt.push_back(i);
        for(int j = 0;j < n; j++) {
            tmp.clear();
            for(int k = 0;k < vt.size(); k++) {
                if(vt[k]==0) {
                    tmp.push_back(0);
                    tmp.push_back(1);
                } else if(vt[k]==1) {
                    if(n-j-1==0) tmp.push_back(1), tmp.push_back(2);
                    else {
                        tmp.push_back(2); tmp.push_back(1);
                    }
                } else {
                    if(n-j-1 > 1) {
                        tmp.push_back(2);
                        tmp.push_back(0);
                    } else {
                        tmp.push_back(0); tmp.push_back(2);
                    }
                }
            }
            vt.clear();
            for(int k = 0;k < tmp.size(); k++)
                vt.push_back(tmp[k]);
        }
        for(int j = 0;j < 3; j++) cnt[j] = 0;
        for(int j = 0;j < vt.size(); j++) cnt[vt[j]]++;
        if(cnt[0]==p && cnt[1] == r && cnt[2] == s) {
            string cur = "";
            for(int j = 0;j < vt.size(); j++) {
                if(vt[j]==0) cur += 'P';
                else if(vt[j]==1) cur += 'R';
                else    cur += 'S';
            }
            if(ans == "" || cur < ans) ans = cur;
        }
    }
    if(ans == "") return false;
    cout<<ans<<endl;
    return true;
}

int main() {
     freopen("A-small.in", "r", stdin);
     freopen("A-small.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        printf("Case #%d: ", ++cas);
        if(!solve()) puts("IMPOSSIBLE");
    }
    return 0;
}
