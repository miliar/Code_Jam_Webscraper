#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a), __ = (b); i < __; ++i)	
#define st first
#define nd second
#define dbg(x) cout << #x << " " << x << endl
using namespace std;

const double eps = 1e-7;
const int inf = 0x3f3f3f3f;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<int> vi;

string str[105];
char ordem[105];
int ind;
vector<int> tam[105];

int main() {
    int nt; scanf("%d", &nt); ++nt;
    fr(_,1,nt) {
        int n; scanf("%d", &n);
        fr(i,0,n) {
            cin >> str[i];
            tam[i].clear();
        }
        ind = 0;
        ordem[ind++] = str[0][0];
        int len = 1;
        fr(i,1,str[0].size()) {
            if (str[0][i] != ordem[ind-1]) {
                tam[0].push_back(len);
                ordem[ind++] = str[0][i];
                len = 1;
            } else ++len;
        }
        tam[0].push_back(len);
        bool ok = true;
        fr(i,1,n) {
            int at = 0;
            char prev = str[i][0];
            len = 1;
            if (prev != ordem[0]) {ok = false; break;}
            fr(j,1,str[i].size()) {
                if (str[i][j] != prev) {
                    ++at;
                    prev = str[i][j];
                    tam[i].push_back(len);
                    len = 1;
                    if (prev != ordem[at]) {
                        ok = false; break;
                    }
                } else ++len;
            }
            ok &= at == ind-1;
            tam[i].push_back(len);
            if (!ok) break;
        }
        printf("Case #%d: ", _);
        if (!ok) puts("Fegla Won");
        else {
            int ans = 0;
            fr(j,0,ind) {
                int sum = 0;
                fr(i,0,n) {
                    sum += tam[i][j];
                }
                sum /= n;
                fr(i,0,n) {
                    ans += abs(tam[i][j] - sum);
                }
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}
