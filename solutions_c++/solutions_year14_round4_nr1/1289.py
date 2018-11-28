#define _USE_32BIT_TIME_T 1
#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

int result(int X, vector<int>& v)
{
    //DEBUG(X);
    sort(v.rbegin(), v.rend());
    int cnt = 0;
    for (int i = 0; i < v.size(); ++i) {
        ++cnt;
        int cur = v[i];
        int lo = i + 1, hi = v.size() - 1;
        if (i + 1 == v.size())
            break;
        else if (v[lo] + cur <= X)
            ++i;
        else if (v[hi] + cur > X)
            continue;
        else {
            while (lo + 1 != hi) {
                int mid = (lo + hi) / 2;
                if (v[mid] + cur > X)
                    lo = mid;
                else
                    hi = mid;
            }
            v.erase(v.begin() + hi);
        }
    }
    return cnt;
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        int N, X;
        cin >> N >> X;
        vector<int> S(N);
        for (int j = 0; j < N; ++j) {
            cin >> S[j];
        }
        cout << "Case #" << i << ": " << result(X, S) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
