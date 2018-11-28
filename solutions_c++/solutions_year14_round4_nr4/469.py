#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

const int maxm = 10;

int n, m;
string s[maxm];
int server[maxm];
int ans, ways;

void rec(int i)
{
    if (i == m) {
        int tmp = 0;
        for (int j = 0; j < n; j++) {
            set<string> st;
            for (int k = 0; k < m; k++) {
                if (server[k] != j) continue;
                for (int ch = 0; ch <= s[k].length(); ch++) {
                    st.insert(s[k].substr(0, ch));
                }
            }
            tmp += st.size();
        }
        if (tmp > ans) {
            ans = tmp;
            ways = 1;
        } else if (tmp == ans) {
            ways++;
        }
    } else {
        for (int j = 0; j < n; j++) {
            server[i] = j;
            rec(i+1);
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for (int sc = 0; sc < T; sc++) {
        int i, j, k;
        cin >> m >> n;
        for (i = 0; i < m; i++) {
            cin >> s[i];
        }

        ans = 0; ways = 0;
        rec(0);
         
        cout << "Case #" << sc+1 << ": ";
        cout << ans << " " << ways;
        cout << endl;
        }
    
    return 0;
}
