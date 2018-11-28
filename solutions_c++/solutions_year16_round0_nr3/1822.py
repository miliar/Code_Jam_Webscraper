#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
using namespace std;

typedef long long LL;
#define CLR(a,b) memset(a,b,sizeof(a))
int n, j;
struct binary {
    binary() {}
    binary(LL x, int l) {
        for (int i = 0; i < l; ++i) {
            digit.push_back(x % 2);
            x /= 2;
        }
    }
    LL getVal(int w) {
        LL x = 0;
        for (int i = 0; i < digit.size(); ++i) {
            x *= w;
            x += digit[i];
        }
        return x;
    }
    vector<int> digit;
};
void out(vector<int> digit) {
    for (auto& v : digit) {
        printf("%d",v);
    }
}
void solve()
{
    int cnt = 0;
    vector<int> pattern_length = vector<int> {16};
    for (auto& pattern : pattern_length) {
        int left = pattern - 2;
        for (int i = 0; i < (1 << left); ++i) {
            if (cnt >= j) break;
            binary val;
            val.digit.push_back(1);
            auto middle = binary(i, left);
            for (auto& v : middle.digit) {
                val.digit.push_back(v);
            }
            val.digit.push_back(1);
            binary v;
            for (int i = 0; i < 32 / pattern; ++i) {
                for (auto& x : val.digit) {
                    v.digit.push_back(x);
                }
            }
            out(v.digit);
            for (int w = 2; w <= 10; ++w) {
                LL fac = val.getVal(w);
                printf(" %lld",fac);
            }
            puts("");
            cnt ++;
        }
    }
}

int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d:\n", ++cas);
        scanf("%d %d", &n, &j);
        solve();
    }
    return 0;
}