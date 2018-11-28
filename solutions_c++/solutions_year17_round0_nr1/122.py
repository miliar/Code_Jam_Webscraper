#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iomanip>
#include <map>
#include <cmath>
#include <deque>
using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int maxn = 200010;
const double eps = 1e-8;

int T;
string s;
int n;
int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        cin >> s >> n;
        int ans = 0;
        for (int i = 0; i < s.length()-n+1; i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = i; j < i+n; j++) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
            }
        }
        bool ok = 1;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-') {
                ok = 0;
            }
        }
        if (ok) {
            printf("%d\n",ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
