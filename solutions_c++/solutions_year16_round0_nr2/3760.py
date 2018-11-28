#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>

#define _ << " " <<
#define trace(x) cout << "# " << x << endl

using namespace std;

typedef long long Long;

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string pank;
        cin >> pank;
        int ans = 0;
        int N = pank.size();
        if (N == 1) {
            ans = (pank[0] == '-') ? 1 : 0;
        }
        else {
            int end = N - 1;
            while (pank[end] == '+') end--;
            end++;
            int start = 0;
            int cross = 0, dash = 0;
            for (int i = 0; i <= end; i++) {
                if (pank[i] == '+') {
                    cross++;
                    if (dash>0) {
                        ans++;
                        dash=0;
                    }
                }
                else {
                    dash++;
                    if (cross>0) {
                        ans++;
                        cross=0;
                    }
                    if (i == end)
                        ans++;
                }
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}