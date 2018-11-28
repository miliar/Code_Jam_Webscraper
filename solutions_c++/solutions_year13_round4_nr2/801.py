#include <iostream>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int main() {
#define int long long
    ifstream cin("B-small-attempt0.in");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, P;
        cin >> N >> P;
        if (P == (1<<N)) {
            cout.precision(15);
            cout << "Case #" << t << ": ";
            cout << (1<<N)-1 << " " << (1<<N)-1;
            cout << endl;
            continue;
        }
        vector<int> p(N);
        int cur = 0;
        int all = 0;
        while (P > 0) {
            p[N-1-cur] = P & 1;
            P >>= 1;
            all += p[N-1-cur];
            cur++;
        }
        int num = 0;
        for (int i = 0; i < N; i++) {
            if (p[i])
                num++;
            else
                break;
        }
        num -= (all == num);
        int res2 = 0;
        for (int i = 0; i < N; i++) {
            if (p[i] == 0)
                res2++;
            else
                break;
        }
        res2 ++; // = (all == N - res2);
        //cout << all << endl;
        //cout << res2 << endl;
        res2 = (1 << N) - (1 << (res2));
        cout.precision(15);
        cout << "Case #" << t << ": ";
        cout << (1 << (num+1) ) - 2 << " " << res2;
        cout << endl;
    }
}

