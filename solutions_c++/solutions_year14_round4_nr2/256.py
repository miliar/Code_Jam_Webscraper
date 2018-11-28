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

int solve()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n; ++i)
        cin >> a[i];

    int ret = 0;
    for(int i=0; i<n; ++i){
        int k = min_element(a.begin(), a.end()) - a.begin();
        ret += min(k, n - 1 - i - k);
        a.erase(a.begin() + k);
    }

    return ret;
}

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        int ret = solve();
        cout << "Case #" << tc << ": " << ret << endl;
    }

    return 0;
}