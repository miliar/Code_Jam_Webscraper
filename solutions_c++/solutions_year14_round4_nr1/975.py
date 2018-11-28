#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
	int T;
    cin >> T;

    for (int t=1; t <= T; ++t) {
        int N, X;
        cin >> N >> X;
//        N = 10000;
//        X = 1;

        vector <int> v(N);
        vector <bool> used(N, false);
        for (int i=0; i < N; ++i) {
            cin >> v[i];
//            v[i] = 1;
        }

        sort(v.begin(), v.end());

        int ans = 0;

        for (int i=N-1; i >= 0; --i) {
            if (!used[i]) {
                for (int j=i-1; j >= 0; --j) {
                    if (!used[j] && v[i] + v[j] <= X) {
                        used[j] = true;
                        break;
                    }
                }
                used[i] = true;
                ++ans;
            }
        }

        cout << "Case #" << t << ": " << ans << endl;
    }
	
	return 0;
}
