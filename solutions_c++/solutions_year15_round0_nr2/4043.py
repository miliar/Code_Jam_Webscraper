#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int N;
map<pair<int, vector<int> >, int> dp;

int solve(int time, const vector<int>& cakes) {
    if(cakes.empty())
        return time;
    if(dp.find({time, cakes}) != dp.end())
        return dp[{time, cakes}];

    vector<int> newCakes;
    for(int c : cakes)
        if(c-1 > 0)
            newCakes.push_back(c-1);
    int res = solve(time+1, newCakes);

    int maxCake = cakes.back();
    int maxIndex = cakes.size()-1;

    if(maxCake > 1)
        for(int j=1;j<maxCake;++j) {
            newCakes = cakes;
            newCakes[maxIndex] = maxCake-j;
            newCakes.push_back(j);
            sort(newCakes.begin(), newCakes.end());
            res = min(res, solve(time+1, newCakes));
        }
        
    dp[{time, cakes}] = res;
    return res;
}

int main() {
    int tc;
    scanf("%d", &tc);
    for(int ii=1;ii<=tc;++ii) {
        dp.clear();
        scanf("%d", &N);

        vector<int> arr;
        for(int i=0;i<N;++i) {
            int a;
            scanf("%d", &a);
            arr.push_back(a);
        }

        sort(arr.begin(), arr.end());
        int ans = solve(0, arr);

        printf("Case #%d: %d\n", ii, ans);
    }
    return 0;
}
