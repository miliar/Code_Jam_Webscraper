#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

int test(VI& vals, int s, int f, int mul)
{
    if (f - s <= 1)
        return 0;
    VI t;
    for (int i = s; i < f; i++)
        t.push_back(vals[i] * mul);
    bool good = false;
    int ret = 0;
    while (!good) {
        good = true;
        for (int i = 0; i < t.size() - 1; i++)
            if (t[i] > t[i+1]) {
                swap(t[i], t[i+1]);
                ret++;
                good = false;
            }
    }
    return ret;
}

int main(int argc, const char* argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        VI vals;
        int best = 1000*1000*1000;
        cin >> N;
        vals.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> vals[i];
        }
        if (N == 1) {
            best = 0;
            goto done;
        }
        for (int m = 0; m < (1 << N); m++) {
            VI left, right;
            int bonus = 0;
            for (int i = 0; i < N; i++) {
                if (m & (1 << i)) {
                    left.push_back(vals[i]);
                    bonus += right.size();
                } else {
                    right.push_back(vals[i]);
                }
            }
            best = min(best, bonus + test(left, 0, left.size(), 1) + test(right, 0, right.size(), -1));
        }
done:
        cout << "Case #" << t << ": " << best << endl;
    }
    return 0;
}
