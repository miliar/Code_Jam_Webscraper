#include <iostream>
#include <cstdio>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

bool isPalin(long long x) {
    stringstream ss; ss << x;
    string s = ss.str();
    string t = s; reverse(t.begin(), t.end());
    return s == t;
}

void duyet() {
    cout << "{";
    for(long long i = 1; i <= 10001110; ++i)
        if (isPalin(i) && isPalin(i*i))
            cout << i*i << "LL,";
    cout << "}";
}

const long long x[] = {1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,100000020000001LL};

int main() {
    freopen("C.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    // duyet();
    int ntest; cin >> ntest;
    for(int test = 0; test < ntest; ++test) {
        long long l, r; cin >> l >> r;
        int res = 0;
        for(int i = 0; i < 40; ++i)
            if (x[i] >= l && x[i] <= r) {
                ++res;
            }
        cout << "Case #" << test+1 << ": " << res << endl;
    }
    return 0;
}
