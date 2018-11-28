#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 100001;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;

void solve(int ca){
    double c, f, x, sp;
    cin >> c >> f >> x;
    double ret = 1e10;
    sp = 2.0;
    double t = 0, rem = 0;
    while (true){
        if (t >= ret) break;
        ret = min(ret, (x - rem) / sp + t);
        if (rem >= c){
            rem -= c;
            sp += f;
        } else{
            t += (c - rem) / sp;
            sp += f;
            rem = 0;
        }
    }
    printf("Case #%d: %.7lf\n", ca, ret);
}

int main(){
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++){
        solve(i + 1);
    }
    return 0;
}
