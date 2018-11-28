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
        int N;
        cin >> N;

        vector <int> v(N);
        map <int, int> reverse;
        vector <int> sorted(N);
        for (int i=0; i < N; ++i) {
            cin >> v[i];
            sorted[i] = v[i];
            reverse[v[i]] = i;
        }

        sort(sorted.begin(), sorted.end());

        int ans = 0;
        int head = 0;
        int tail = N - 1;

        for (int i=0; i < N; ++i) {
            int k = reverse[sorted[i]];
//            printf("%d) %d %d %d (%d)\n", i, k, head, tail, ans);
            if (k - head < tail - k) {
//                puts("down");
                for (int j=k-1; j >= head; --j) {
                    swap(v[j], v[j + 1]);
                    reverse[v[j]] = j;
                    reverse[v[j + 1]] = j + 1;
                    ++ans;
                }
                ++head;
            } else {
//                puts("up");
                for (int j=k; j < tail; ++j) {
                    swap(v[j], v[j + 1]);
                    reverse[v[j]] = j;
                    reverse[v[j + 1]] = j + 1;
                    ++ans;
                }
                --tail;
            }
        }

        cout << "Case #" << t << ": " << ans << endl;
    }
	
	return 0;
}
