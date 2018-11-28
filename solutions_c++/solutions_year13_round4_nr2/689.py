//#define ONLINE_JUDGE

#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <limits>
#include <queue>
#include <stdexcept>

using namespace std;

typedef long long L;
L twoPow(L n)
{
    L res = 1;
    while (n > 0) {
        res *= 2;
        --n;
    }
    return res;
}

void normalize(L & k, L n) {
    k = min(k, twoPow(n)-1);
    k = max(k, L(0));
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("cin", "r", stdin);

    freopen("out", "w", stdout);
#endif


    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        L n, p;
        cin >> n >> p;
        L gar, pos;

        L pw = twoPow(n), cur = 1;
        L t;
        for (t = n; t >= 0; --t) {
            L r = pw - cur;
            if (r < p)
                break;
            cur *= 2;
        }

        gar = twoPow(t+1)-2;
        normalize(gar, n);

        for (t = 0; ; ++t) {
            L r = pw - 1;
            if (r < p)
                break;
            pw /= 2;
        }

        pos =  twoPow(n)-twoPow(t);

        normalize(pos, n);


        cout << "Case #" << cas << ": ";
        cout << gar << ' ' << pos << endl;
    }


#ifndef ONLINE_JUDGE
    fclose(stdin);
    putchar('\n');
#endif
}

