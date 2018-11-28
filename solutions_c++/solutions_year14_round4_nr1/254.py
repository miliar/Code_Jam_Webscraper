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
    int n, x;
    cin >> n >> x;
    vector<int> s(n);
    for(int i=0; i<n; ++i)
        cin >> s[i];
    sort(s.begin(), s.end());

    int i = 0;
    int j = n - 1;
    int ret = 0;
    while(i <= j){
        if(s[i] + s[j] <= x){
            ++ i;
            -- j;
        }
        else{
            -- j;
        }
        ++ ret;
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