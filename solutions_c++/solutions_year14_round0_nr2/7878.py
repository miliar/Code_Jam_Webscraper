#include <cstdio>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#ifdef DEBUG
    int __msg_cnt = 0;
    #define msg(x) cerr<<++__msg_cnt<<" "<<__FUNCTION__<<"("<<__LINE__<<"): "<<x<<endl;
#else
    #define msg(x)
#endif

template<typename T>
inline void maximize(T& a, const T b) {
    if (b > a) a = b;
}
template<typename T>
inline void minimize(T& a, const T b) {
    if (b < a) a = b;
}

int scan() {
    char ch;
    int seg = 0;
    while (!isdigit(ch = getchar()))
        seg |= (ch == '-');
    int x = ch - '0';
    while (isdigit(ch = getchar()))
        x = x * 10 + ch - '0';
    return x;
}

double work() {
    double c, f, x, r = 2.0;
    cin>> c>> f>> x;
    r /= f;
    double ans = x / r;
    double tmp = 0.0;
    for (int n = 0; ; ++n) {
        tmp += c / (n + r);
        double t = tmp + x / (n + 1 + r);
        if (t > ans) break;
        ans = t;
    }
    return ans / f;
}

int main() {
    cout.precision(8);
    cout<< fixed;
    int z = scan();
    for (int i = 1; i <= z; ++i)
        cout<< "Case #"<< i<< ": "<< work()<< endl;
    return 0;
}
