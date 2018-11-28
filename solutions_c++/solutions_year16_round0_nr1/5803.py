/*
 * new
 *      Author: AbdullaAshraf
 */
#include<bits/stdc++.h>
using namespace std;
const int OO = 1000000000;
const int maxn = 1e5 + 5;

typedef long long ll;
#define REP(i,n) for(int(i)=0; (i)<(n); (i)++)

set<int> seen;

void getd(ll x) {
	if (x == 0)
		seen.insert(0);
	while (x > 0) {
		seen.insert(x % 10);
		x /= 10;
	}
}

int main(void) {
	ofstream sout ("output.txt");
	ifstream sin ("A-small-attempt0.in");
	int T;
	sin >> T;
	REP(i,T)
	{
		seen.clear();
		ll n = 0, t = 0;
		sin >> n;
		if (n == 0){
			sout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		while (true) {
			t += n;
			getd(t);
			if (seen.size() == 10)
				break;
		}
		sout << "Case #" << i+1 << ": " << t;
		if (i!=T-1) sout << endl;
	}
	return 0;
}
