#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

long long createPalin(int i, bool mode)
{
    int work = i;
    long long res = i;
    if (mode == 1)
        work /= 10;
    while (work > 0) {
        res *= 10;
        res += work % 10;
        work /= 10;
    }
    return res;
}

bool checkPalin(long long p) {
    long long rev = 0;
    long long work = p;
    while (work > 0) {
        rev *= 10;
        rev += work % 10;
        work /= 10;
    }
    return rev == p;
}

int main()
{
    vector<long long> vals;
    for (int i = 0; i < 1000000; ++i) {
        long long p = createPalin(i, 0);
        if (checkPalin(p*p))
            vals.push_back(p*p);
        p = createPalin(i, 1);
        if (checkPalin(p*p))
            vals.push_back(p*p);
    }
    sort(vals.begin(), vals.end());
    int T;
    cin >> T;
    for (int k = 1; k <= T; ++k) {
        long long a,b;
        int count = 0;
        cin >> a >> b;
        for (int i = 0; i < vals.size(); ++i)
            if (a <= vals[i] && vals[i] <= b)
                ++count;
        cout << "Case #" << k << ": " << count << endl;
    }
}
