#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Up and down
int main()
{
    string line;

    int cases;
    cin >> cases;

    for (int caseno = 1; caseno <= cases; caseno++) {
        int N;
        cin >> N;
        vector <int> S(N);
        for (int i = 0; i < N; i++) {
            cin >> S[i];
        }
        int ret = 0;
        while (S.size() > 1) {
            int p = -1;
            for (int i = 0; i < S.size(); i++) {
                if (p == -1 || S[i] < S[p]) {
                    p = i;
                }
            }
            ret += min(p, (int)S.size() - p - 1);
            S.erase(S.begin() + p);
        }
        cout << "Case #" << caseno << ": " << ret << endl;
    }

    return 0;
}
