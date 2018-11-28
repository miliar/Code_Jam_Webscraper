
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
int a, b;

double m1[1005], m2[1005];

int cal(double *m1, double *m2) {
    sort(m1, m1 + n);
    sort(m2, m2 + n);
    
    int res = 0;
    int j = 0;
    REP(i, n) {
        while(j < n && m2[j]< m1[i]) j ++;
        
        if(j < n) {
            res ++;
            
            j ++;
        }
    }
    return res;
}
int main() {
    scanf("%d", &t);
    OREP(c, t) {
        scanf("%d", &n);
        
        REP(i, n) scanf("%lf", m1+i);
        REP(i, n) scanf("%lf", m2+i);
        
        a = cal(m2, m1);
        b = n - cal(m1, m2);
        
        printf("Case #%d: %d %d\n", c, a, b);
    }
    return 0;
}
