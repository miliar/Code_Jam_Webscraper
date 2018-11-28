#include <bits/stdc++.h>
using namespace std;

#define f(i, a, b) for(int i = (a); i < (b); i++)
#define rep(i, b) f(i, 0, b)
#define fa(i, v) for(auto& i : v)
#define sz(x) (int)(x).size()
#define pl(x) cout << #x << " = " << x << endl;
#define pe(x) cout << #x << " = " << x << ", ";
#define pn(x) cout << #x;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
void pv(vi v) {
    fa(o, v) cout << o << " ";
    cout << endl;
}

ifstream in("A-large.in");
ofstream out("Al.out");

void solve() {
    int n;
    in >> n;
    vi members(n);
    int sum = 0;
    rep(i, n) {
        in >> members[i];
        sum += members[i];
    }
    vi order(sum);
    rep(i, sum) {
        int t = distance(members.begin(), max_element(members.begin(), members.end()));
        order[i] = t;
        members[t]--;
    }
    if (!(sum%2)) rep(i, sum/2) {
        out << (char)(order[i*2]+'A') << (char)(order[i*2+1]+'A') << " ";
    } else {
        out << (char)(order[0]+'A') << " ";
        f(i, 1, sum/2+1) {
            out << (char)(order[i*2-1]+'A') << (char)(order[i*2]+'A') << " ";
        }
    }
    out << endl;
}

int main() {
	int N;
	in >> N;
	f(i,0,N) {
		out << "Case #" << i+1 << ": ";
		solve();
	}
    return 0;
}
