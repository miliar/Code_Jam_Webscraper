#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <cassert>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>

using namespace std;

long long countC(long long r, long long t) {
    long long ans = 0;
    while((4*ans+2)*(ans+1)/2 + 2*r*(ans+1) <= t) {
        ans++;
    }
//    if((4*ans+2)*(ans+1)/2 + 2*r*(ans+1) == t) {
//        return ans+1;
//    }
//    else {
//        return ans;
//    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int c = 1; c < T+1; c++) {
        long long r, t;
        cin >> r >> t;
        cout << "Case #" << c << ": " << countC(r,t) << endl;
    }

    return 0;
}

