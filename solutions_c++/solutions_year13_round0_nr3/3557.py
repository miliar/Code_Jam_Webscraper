#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

long long flip(long long n)
{
    long long a, b;

    a = n;
    b = 0;
    while (a > 0) {
        b = b*10 + (a % 10);
        a /= 10;
    }
    return b;
}

bool is_palin(long long n)
{
    long long a;

    return (n == flip(n));
}

int digit(long long n)
{
    long long m;
    int d = 1;

    m = 10;
    while (n >= m) {
        m *= 10;
        d++;
    }
    return d;
}

long long calc(long long N)
{
    long long ret, t, tt;
    long long i;
    long long l, h;

    ret = 0;

    // odd
    l = 1;
    h = 10;
    while (true) {
        for(i=l;i<h;i++) {
            t = (i-(i%10))*l+flip(i);
            tt = t*t;
            if (tt >= N)
                break;
            if(is_palin(tt)) {
                // cout << "tt is " << tt << endl;
                ret++;
            }
        }
        if (tt >= N)
            break;
        l *= 10;
        h *= 100;
    }


    // even
    l = 1;
    h = 10;
    while (true) {
        for(i=l;i<h;i++) {
            t = i*h+flip(i);
            tt = t*t;
            if (tt >= N)
                break;
            if(is_palin(tt)) {
                // cout << "tt is " << tt << endl;
                ret++;
            }
        }
        if (tt >= N)
            break;
        l *= 10;
        h *= 100;
    }

    return ret;
}

int
main(void)
{
    int T;
    int t, i, j;
    long long A, B;
    long long num;

    cin >> T;

    for(t=1;t<=T;t++) {
        cin >> A >> B;

        num = calc(B+1) - calc(A);

        cout << "Case #" << t << ": " << num  << endl;
    }
    
    return 0;
}
