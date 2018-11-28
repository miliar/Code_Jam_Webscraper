//#define __test__aTest__
#ifndef __test__aTest__

#include <vector>
#include <list>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <assert.h>

using namespace std;

#define ll long long
#define MAXN 505

struct Node {
    
};

int main() {
    freopen("/Users/zishirs/Documents/workspace/test/test/test.txt", "r", stdin);
    freopen("/Users/zishirs/Documents/workspace/test/test/output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int index = 1; index <= T; ++index) {
        long double r, t;
        cin >> r >> t;
        long double i = (sqrt((2*r - 1)*(2*r - 1) + 8*t) - (2*r - 1))/4;
        ll ret = (ll)i;
        cout<<"Case #"<<index<<": "<<ret<<endl;
    }
    return 0;
}

#endif

