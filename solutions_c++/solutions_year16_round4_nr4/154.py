#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

bool check(vector<string>& v, bitset<4> usedY, bitset<4> usedX)
{
    int n = v.size();

    for(int y=0; y<n; ++y){
        if(usedY[y])
            continue;
        usedY[y] = true;

        bool ng = true;
        for(int x=0; x<n; ++x){
            if(usedX[x] || v[y][x] == '0')
                continue;
            usedX[x] = true;
            ng = false;

            if(!check(v, usedY, usedX))
                return false;

            usedX[x] = false;
        }
        if(ng)
            return false;

        usedY[y] = false;
    }

    return true;
}

int solve(int n, const vector<string>& v)
{
    int ans = INT_MAX;
    for(int i=0; i<(1<<(n*n)); ++i){
        bitset<16> bs(i);
        int cost = bs.count();

        vector<string> w = v;
        for(int j=0; j<n; ++j){
            for(int k=0; k<n; ++k){
                if(bs[j*n+k])
                    w[j][k] = '1';
            }
        }

        if(check(w, 0, 0))
            ans = min(ans, cost);
    }
    return ans;
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        int n;
        cin >> n;
        vector<string> v(n);
        for(int i=0; i<n; ++i)
            cin >> v[i];

        int ans = solve(n, v);
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}