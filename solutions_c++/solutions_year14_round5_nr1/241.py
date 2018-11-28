#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

double solve()
{
    int n, p, q, r, s;
    cin >> n >> p >> q >> r >> s;
    vector<long long> x(n);
    for(int i=0; i<n; ++i)
        x[i] = (i * p + q) % r + s;
    long long sum = accumulate(x.begin(), x.end(), 0LL);

    if(n == 1)
        return 0;
    if(n == 2)
        return *min_element(x.begin(), x.end()) / (double)sum;

    long long left = *max_element(x.begin(), x.end());
    long long right = LLONG_MAX / 2;
    while(left < right){
        long long mid = (left + right) / 2;
        long long sum = 0;
        long long cnt = 0;
        for(int i=0; i<n; ++i){
            sum += x[i];
            if(sum > mid){
                sum = x[i];
                ++ cnt;
            }
        }

        if(cnt < 3)
            right = mid;
        else
            left = mid + 1;
    }

    return (sum - left) / (double)sum;
}

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        double ret = solve();
        cout.setf(ios_base::fixed, ios_base::floatfield);
        cout << setprecision(10);
        cout << "Case #" << tc << ": " << ret << endl;
    }

    return 0;
}