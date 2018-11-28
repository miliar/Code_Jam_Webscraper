#include <bits/stdc++.h>

using namespace std;

#define     mp              make_pair
#define     fs              first
#define     sc              second
#define     pob             pop_back
#define     pub             push_back
#define     eps             1E-7
#define     sz(a)           a.size()
#define     count_one       __builtin_popcount;
#define     count_onell     __builtin_popcountll;
#define     fastIO          ios_base::sync_with_stdio(false)
#define     PI              (acos(-1.0))
#define     linf            (1LL<<62)//>4e18
#define     inf             (0x7f7f7f7f)//>2e9

#ifndef ONLINE_JUDGE
ifstream fin("D:/C++/in");
ofstream fout("D:/C++/out");
#endif

#define NR_I 2
#define NR_J 3
#define NR_K 4

const int MAXN = 10010;
int T;
int l, x, sz;
string v;
int firstk;
vector<int> resi;
bitset<MAXN> resk;

int multiply(int x, int y) {
    if(x < 0)
        return -1 * multiply(-x, y);
    if(y < 0)
        return -1 * multiply(x, -y);
    if(x == 1)
        return y;
    if(y == 1)
        return x;
    if(x == y)
        return -1;
    if(x == NR_I && y == NR_J)
        return NR_K;
    if(x == NR_J && y == NR_I)
        return -NR_K;
    if(x == NR_I && y == NR_K)
        return -NR_J;
    if(x == NR_K && y == NR_I)
        return NR_J;
    if(x == NR_J && y == NR_K)
        return NR_I;
    if(x == NR_K && y == NR_J)
        return -NR_I;
}

int getch(int pos) {
    return (v[pos] - 'i' + 2);
}

string solve() {
    resi.clear();
    resk.reset();
    /// get i's
    int ans = 1;
    for(int i = 0; i < sz - 2; ++i) {
        ans = multiply(ans, getch(i));
        if(ans == NR_I)
            resi.pub(i + 1);
    }
    if(resi.empty())
        return "NO";

    ans = 1;
    firstk = 0;
    for(int i = sz - 1; i >= 0; --i) {
        ans = multiply(getch(i), ans);
        if(ans == NR_K) {
            if(!firstk)
                firstk = i;
            resk[i] = true;
        }
    }

    if(!firstk) {
        return "NO";
    }

    for(auto it : resi) {
        ans = 1;
        for(int i = it; i < firstk; ++i) {
            ans = multiply(ans, getch(i));
            if(ans == NR_J && resk[i + 1] == true)
                return "YES";
        }
    }

    return "NO";
}

void read() {
	fin >> T;
	string aux;
	for(int t = 1; t <= T; ++t) {
        v.clear(); aux.clear();
        fin >> l >> x;
        fin >> aux;
        sz = l * x;
        while(x--)
            v.append(aux);
        fout << "Case #" << t << ": " << solve() << "\n";
	}
}

int main() {
	read();

    return 0;
}
