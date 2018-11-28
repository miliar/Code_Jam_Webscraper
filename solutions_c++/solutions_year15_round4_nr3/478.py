#include <iostream>
#include <map>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int n;
vector<int>S[1110];
map<string, int>Hash;
int eng[2000];
int fran[2000];
int teng[2000], tfran[2000];
vector<int>ALL;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--) {
        Hash.clear();
        ALL.clear();
        scanf("%d", &n);
        char str[20];
        char ch;
        int cnt = 0;
        int now = 0;
        cerr<<T<<endl;
        while(1) {
            scanf("%s%c", str, &ch);
            string s = string(str);
            if(Hash[s] == 0) {
                now++;
                Hash[s] = now;
                fran[now] = 0;
                eng[now] = 0;
                ALL.push_back(now);
               // cout<<s<<" "<<now<<endl;
            }

            if(cnt == 0) {
                eng[Hash[s]] = 1;
            }
            if(cnt == 1) {
                fran[Hash[s]] = 1;
            }
            S[cnt].push_back(Hash[s]);
            if(ch == ' ') {
            } else {
                cnt++;
            }
            if(cnt == n) {
                break;
            }
        }
        //cout<<fran[5]<<" "<<eng[5]<<endl;
        for(int i = 0; i < 2000;  i++) {
            tfran[i] = fran[i];
            teng[i] = eng[i];
        }
        int ans = 10000000;
        for(int mask = 0; mask < (1 << (n - 2)); mask++) {
            for(int i = 0; i < 2000;  i++) {
                fran[i] = tfran[i];
                eng[i] = teng[i];
            }
            for(int j = 0; j < n - 2; j++) {
                for(int g = 0; g < S[j + 2].size(); g++) {
                    int id = S[j + 2][g];
                    if(mask & (1<<j)) {
                        eng[id] = 1;
                    } else {
                        fran[id] = 1;
                    }
                }
            }
            int cnt = 0;
            for(int i = 0; i < ALL.size(); i++) {
                //cout<<ALL[i]<<":"<<eng[ALL[i]]<<" "<<fran[ALL[i]]<<endl;
                if(eng[ALL[i]] && fran[ALL[i]]) {
                    cnt++;
                }
            }
            ans = min(ans, cnt);
        }


        printf("Case #%d: %d\n", ++cas, ans);



        for(int i = 0; i < n; i++) {
            S[i].clear();
        }

    }
    return 0;
}
