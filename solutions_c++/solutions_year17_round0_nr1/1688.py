#include <bits/stdc++.h>

using namespace std;

#define D(x) x
#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define REPR(i,a,b) for (int i = (b) - 1; i >= (a); --i)
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int> > VII;

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

int main() {
    ios_base::sync_with_stdio(false);
    cout << setprecision(12) << fixed;

    int T; fin >> T;
    bool arr[2000];
    REP(t,1,T+1) {
        string s; fin >> s;
        int l; fin >> l;
        REP(i,0,s.length()) {
            arr[i] = s[i] == '+';
        }
        int res = 0;
        REP (i,0,s.length()-l+1) {
            if (!arr[i]) {
                res++;
                REP(j,0,l)
                    arr[i+j] = !arr[i+j];
            }
        }
        bool valid = true;
        REP (i,0,s.length()) {
            if (!arr[i]) {
                valid = false;
            }
        }

        if (valid)
            fout << "Case #" << t << ": " << res << endl;
        else
            fout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }

	return 0;
}
