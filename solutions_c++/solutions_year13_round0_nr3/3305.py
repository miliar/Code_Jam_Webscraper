#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <sstream>
#include <ctime>
#include <set>
#define  N   362
#define  M   1200
#define  inf 0XFFFFFFFFFFFFFFll
#define  mod 1000000007
#define  LL  long long
#define  eps 1e-12
#define  pi  acos(-1.0)

using namespace std;


ifstream fi("C-small-attempt1.in");
#define cin fi
ofstream fo("C-small-attempt1.out");
#define cout fo

int a[40];

bool is(LL n) {
    int cnt = 0;
    while (n) {
        a[cnt++] = n%10;
        n /= 10;
    }
    for (int i=0; i<cnt/2; i++)
        if (a[i] != a[cnt-1-i])
            return false;
    return true;
}
void mp(LL n, LL &n1,LL &n2) {
    int cnt = 0;
    n1 = n2 = 0;
    while (n) {
        a[cnt++] = n%10;
         n /= 10;
    }
    for (int i=0; i<cnt; i++)
        a[cnt+i] = a[cnt-1-i];
    for (int i=0; i<cnt*2; i++)
        n1 = n1*10 + a[i];
    for (int i=1; i<cnt; i++)
        a[cnt+i-1] = a[cnt-1-i];
    for (int i=0; i<cnt*2-1; i++)
        n2 = n2*10 + a[i];
}

LL w[22222], all = 0;

int main()
{
    for (int i=0; i<=9999; i++) {
        LL n1, n2;
        if (i % 10 == 0)
            continue;
        mp(i, n1, n2);
        if (is(n1)&&is(n1*n1))
            w[all++] = n1*n1;
        if (is(n2)&&is(n2*n2))
            w[all++] = n2*n2;
    }
    sort(w, w+all);
    int cases; cin >> cases;
    for (int c=1; c<=cases; c++) {
        cout << "Case #" << c << ": ";
        LL a, b; cin >> a >> b;
        a = upper_bound(w, w+all, a-1) - w;
        b = upper_bound(w, w+all, b) - w;
        cout << b - a << endl;
    }
    return 0;
}

