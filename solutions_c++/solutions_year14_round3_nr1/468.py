#include <sstream>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b) {
 if (b==0) return a;
 return gcd(b, a%b);
}

void solve(long long P, long long Q) {
	while (gcd(P,Q)>1) {
		long long tmp=gcd(P,Q);
		P/=tmp;
		Q/=tmp;
	}
	long long tq=Q;
	if (Q==1) {
		cout << 1;
		return;
	}
	while (tq%2==0)
		tq/=2;
	if (tq!=1) {
		cout << "impossible";
		return;
	}
	long long divi=2;
	for (int i=1; i<40; i++) {
		if (P>=Q/divi) {
			cout << i;
			return;
		}
		divi*=2;
	}
    return;
}

int main() {
//    freopen("A-small-attempt0.in", "rt", stdin);
//    freopen("A-small.out", "wt", stdout);
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
//	freopen("test.in", "rt", stdin);
   
    int T;
    cin>>T;

    for (int i=1; i<=T; i++) {
        long long P, Q;
		char tmp;
		cin >> P >> tmp >> Q;
        cout << "Case #" << i << ": ";
		solve(P,Q);
		cout << endl;
    }
}