#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define For(i, n) for (int i = 0; i < (int) n; ++i)
#define SIZE(x) ((int) (x).size())
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef DG
#define DG 0
#endif
#define LOG(...) (DG ? fprintf(stderr, __VA_ARGS__) : 0)

set <ll> results;
ll n, j;

void print_temp(ll temp) {
    string res;
    For(i, n) {
        res.push_back('0' + (temp & 1));
        temp >>= 1;
    }
    reverse(res.begin(), res.end());
    cout << res;
}

void print_divs(ll polydiv) {
    for (int i = 2; i <= 10; i++) {
        ll exp = 1, res = 0, polycopy = polydiv;
        while (polycopy > 0) {
            res += (polycopy & 1) * exp;
            exp *= i;
            polycopy >>= 1;
        }
        cout << ' ' << res;
    }
    cout << '\n';
}

void recurse(ll temp, ll polydiv, ll lenpoly, ll shift) {
    if (shift == 0) {
        if (results.count(temp) == 0) {
            print_temp(temp);
            print_divs(polydiv);
            results.insert(temp);
            if (results.size() == j) exit(0);
        }
        return;
    }
    if (temp & (polydiv << shift)) return recurse(temp, polydiv, lenpoly, shift - 1);
    recurse(temp, polydiv, lenpoly, shift - 1);
    recurse(temp | (polydiv << shift), polydiv, lenpoly, shift - 1);
}

int main(){
    int t;
    cin >> t;
    cin >> n >> j;
    printf("Case #1:\n");
    for(ll i = 1; i < ( 1 << (n - 2)); i++) {
        ll length = 0, copyi = i, copy2i;
        ll temp = (1<<(n - 1)) + 1;
        copyi <<= 1;
        copyi ++;
        copy2i = copyi;
        while (copy2i != 0) {
            length ++;
            copy2i >>= 1;
        }
        recurse(temp | copyi | (copyi << (n - length)), copyi, length, n - length);

    }

}
