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

const int MAXN = 100;

void read() {
    int T, x, sum, toAdd;
    char c;

	cin >> T;
	for(int t = 1; t <= T; ++t) {
        cin >> x;
        sum = 0;
        toAdd = 0;
        for(int i = 0; i <= x; ++i) {
            cin >> c;
            int pers = c - '0';

            if(sum < i && pers > 0)
                toAdd += (i - sum), sum += (i - sum);
            sum += pers;
        }
        cout << "Case #" << t << ": " << toAdd << "\n";
	}
}

int main() {
	read();

    return 0;
}
