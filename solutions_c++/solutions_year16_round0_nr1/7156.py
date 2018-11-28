#include <bits/stdc++.h>
#define ll long long
#define oo 100000000000
using namespace std;
ifstream fin("a.in");
ofstream fout("a.out");
int T, t;
ll x, nn, n;
set<int>s;
int main() {
    fin >> T;

    for(t = 1; t <= T; t++) {
        s.clear();
        fin >> n;
        fout << "Case #" << t << ": ";

        if(n == 0) {
            fout << "INSOMNIA\n";
            continue;
        }

        nn = n;
        x = n;

        while(x) {
            s.insert(x % 10);
            x /= 10;
        }

        while(s.size() != 10) {
            nn += n;
            x = nn;

            while(x) {
                s.insert(x % 10);
                x /= 10;
            }
        }

        fout << nn << '\n';
    }

    return 0;
}
