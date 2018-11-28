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

int solve1(const vector<double>& a, const vector<double>& b)
{
    int n = a.size();
    int ret = 0;
    int j = 0;
    for(int i=0; i<n; ++i){
        if(a[i] > b[j]){
            ++ ret;
            ++ j;
        }
    }
    return ret;
}

int solve2(const vector<double>& a, const vector<double>& b)
{
    int n = a.size();
    int ret = 0;
    multiset<double> ms(b.begin(), b.end());
    for(int i=0; i<n; ++i){
        auto it = ms.upper_bound(a[i]);
        if(it == ms.end()){
            ms.erase(ms.begin());
            ++ ret;
        }
        else{
            ms.erase(it);
        }
    }
    return ret;
}

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        int n;
        cin >> n;
        vector<double> a(n), b(n);
        for(int i=0; i<n; ++i)
            cin >> a[i];
        for(int i=0; i<n; ++i)
            cin >> b[i];
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        cout << "Case #" << tc << ": " << solve1(a, b) << ' ' << solve2(a, b) << endl;
    }

    return 0;
}