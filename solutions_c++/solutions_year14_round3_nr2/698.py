#include <iostream>
#include <cstring>
#include <cstdio>

#define MOD 1000000007

using namespace std;

long long mem[1054][30];
int n;
string s[11];
int vis[30];

long long solve(int mask, int last) {
    if(mem[mask][last] != -1) return mem[mask][last];
    if(mask == 0) return 1;
    long long ans = 0;
    for(int i = 0; i < n; i++) {
        if(mask&(1<<i)) {
            memset(vis, 0, sizeof(vis));
            if(last == s[i][0]-'a') {
                vis[s[i][0]-'a'] = 1;
                int pos = 0;
                bool flag = true;
                while(s[i][pos]-'a' == last && pos < s[i].size()) pos++;
                for(int j = pos; j < s[i].size();) {
                    int ch = s[i][j]-'a';
                    while(ch == s[i][j]-'a' && j < s[i].size()) {
                        j++;
                    }
                    if(vis[ch]) flag = false;
                    for(int k = 0; k < n; k++) {
                        if(!(mask&(1<<k))) {
                            for(int l = 0; l < s[k].size(); l++) if(s[k][l]-'a' == ch) flag = false;
                        }
                    }
                    vis[ch] = 1;
                }
                if(flag) {
                    ans = (ans + solve(mask^(1<<i), s[i][s[i].size()-1]-'a'))%MOD;
                }
            }
            else {
                int pos = 0;
                bool flag = true;
                for(int j = pos; j < s[i].size();) {
                    int ch = s[i][j]-'a';
                    while(ch == s[i][j]-'a' && j < s[i].size()) {
                        j++;
                    }
                    if(vis[ch]) flag = false;
                    for(int k = 0; k < n; k++) {
                        if(!(mask&(1<<k))) {
                            for(int l = 0; l < s[k].size(); l++) if(s[k][l]-'a' == ch) flag = false;
                        }
                    }
                    vis[ch] = 1;
                }
                if(flag) {
                    ans = (ans + solve(mask^(1<<i), s[i][s[i].size()-1]-'a'))%MOD;
                }
            }
        }
    }
    return mem[mask][last] = ans;
}

int main()
{
    int t;
    freopen("in1.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> t;
    int cs = 0;
    while(t--) {
        cin >> n;
        cs++;
        memset(mem, -1, sizeof(mem));
        for(int i = 0; i < n; i++) {
            cin >> s[i];
        }
        cout << "Case #" << cs << ": ";
        cout << solve((1<<n)-1, 27) << endl;
    }
}
