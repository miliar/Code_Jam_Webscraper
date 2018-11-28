
/*
ID: wengsht1
LANG: C++
TASK: test
*/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <sstream>
#include <set>
using namespace std;

#define MX 100005
#define REP(i,n) for(int i=0;i<(n);i++)
#define OREP(i,n) for(int i=1;i<=(n);i++)

typedef long long          LL;
typedef unsigned long long ULL;
typedef unsigned int       UINT;

int n, m, k, t;

double c, f, x;
int main() {
    cin >> t;
    OREP(ca, t) {
        cin >> c >> f >> x;
        
        double res = 0;
        double velocity = 2.0;
    
        if(c >= x) {
            res = x / velocity;
        }
        else {
            while(x / (velocity + f) + c / velocity < x / velocity) {
                res += c / velocity;
                velocity += f;
            }
            res += x / velocity;
        }
        printf("Case #%d: %.7lf\n", ca, res);
    }
    return 0;
}
