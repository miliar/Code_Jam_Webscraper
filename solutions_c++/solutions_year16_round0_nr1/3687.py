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

using namespace std;

typedef long long Long;

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        set<int> vis;
        if (!N)
            cout << "Case #" << t << ": INSOMNIA" << endl;
        else {
            Long last = N, i = 0, reduce;
            while (1) {
                if (vis.size() == 10) {
                    break;
                }
                last = (Long) (++i * N);
                reduce = last;
                while (reduce > 0) {
                    vis.insert(reduce % 10);
                    reduce /= 10;
                }
            }
            cout << "Case #" << t << ": " << last << endl;
        }
    }
}
