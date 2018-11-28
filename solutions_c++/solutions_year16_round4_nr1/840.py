#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define mp make_pair
#define pb push_back

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define REP(i, n) for(int i = 0; i < (n); ++i)

using namespace std;
typedef long long ll;

char SEQ[5000] = {0, };

int M = 0;

bool test() {    
    string seq = SEQ;
    while(seq.length() > 1) {
        //cout << seq << endl;
        string seq2;
        for(int i = 0; i < seq.length(); i += 2) {
            if (seq[i] == seq[i+1]) return false;

            if (seq[i] == 'P' && seq[i+1] == 'R') seq2 += 'P';
            else if (seq[i] == 'R' && seq[i+1] == 'P') seq2 += 'P';

            else if (seq[i] == 'R' && seq[i+1] == 'S') seq2 += 'R';
            else if (seq[i] == 'S' && seq[i+1] == 'R') seq2 += 'R';

            else if (seq[i] == 'P' && seq[i+1] == 'S') seq2 += 'S';
            else if (seq[i] == 'S' && seq[i+1] == 'P') seq2 += 'S';
        }
        seq = seq2;
    }
    return true;
}

int go(int p, int r, int s) {
    //cout << p << r << s << endl;
    if (p + r + s <= 1) {
        if (p == 1) cout << "P";
        else if (r == 1) cout << "R";
        else if (s == 1) cout << "S";
        return 1;
    }
    int np = p / 2;
    int nr = r / 2;
    int ns = s / 2;

    if (p % 2 == 1) ++np;
    else if (r % 2 == 1) ++nr;
    else ++ns;
    go(np, nr, ns);
    go(p-np,r-nr,s-ns);   
    return 1; 
}


void solve()
{
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    M = R + P + S;
    if (abs(R-P) > 1 || abs(P-S) > 1 || abs(S-R) > 1) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    go(P, R, S);
    cout << endl;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}
