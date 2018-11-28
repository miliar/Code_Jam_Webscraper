#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int k, c, s;
        cout << "Case #" << i << ":";
        cin >> k >> c >> s;
        vector<long long> res;
        if (c >= k) {
            long long t = 0;
            for (int j = 0; j < c; ++j) {
                t *= k;
                if (j < k) {
                    t += j;
                }
            }
            res.push_back(t+1);
        } else {
            long long t = 0;
            for (int j = 0; j < c-1; ++j) {
                t *= k;
                t += j;
            }
            t *= k;

            long long l = t + c - 1;
            long long r = t + k;
            for (long long j = l; j < r; ++j) {
                res.push_back(j+1);
            }
        }
        if (res.size() <= s) {
            for (long long r : res) {
                cout << ' ' << r;
            }
            cout << endl;
        } else {
            cout << " IMPOSSIBLE" << endl;


        }
    }
    return 0;
}

