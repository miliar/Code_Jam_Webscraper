#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <deque>
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
#include <ctime>

using namespace std;

string tostring(long a) {
    string r = "";
    while (a > 0) {
        r.insert(r.end(),'0' + a%10);
        a = a / 10;
    }
    return r;
}

long palin(long x) {
    string s = tostring(x);
    long i;
    long n = s.length();
    for (i = 0; i < n/2; i ++) {
        
        if (s[i] != s[n-i-1]) return 0;
    }
    return 1;
}

long solve( long t) {
    long a,b,i,j;
    cin >>a >> b;
    long cnt = 0;
    for (i = a; i <= b; i ++) {
        if (i == 121) {
            i = 121;
        }
        if (!palin(i)) continue;
        
        long sq = sqrt(i);
        if (sq*sq != i) continue;
        if (palin(sq)) cnt ++;
    }
    printf("Case #%d: %d\n",t+1,cnt);
}

int main () {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    long T,i,j;
    cin >> T;
    for (i = 0; i < T; i ++) {
        solve(i);
    }
    return 0;
}

