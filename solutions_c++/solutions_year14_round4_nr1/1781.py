#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int N, X;
        cin >> N >> X;
        
        multiset<int> files;

        for (int i = 0; i < N ; i++) {
            int f;
            cin >> f;
            files.insert(f);
        }
        //sort(files.begin(), files.end());

        int cds= 0;

        while (!files.empty()) {
            auto lastit = --files.end();
            int last = *(lastit);
            files.erase(lastit);
            int maxsize = X  - last;

            auto it = files.upper_bound(maxsize);
            if (it == files.begin()) {
                cds ++;
            } else {
                it--;
                files.erase(it);
                cds ++;
            }
        }

        printf("Case #%d: %d\n", testcase, cds);
    }

    return 0;
}
