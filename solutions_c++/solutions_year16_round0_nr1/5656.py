#include <iostream>
#include <vector>

#define FOR(it, seq) for(auto it : seq)
#define FORI(it, beg, end) for(auto it = beg; it != end; ++it)

#define DBG(x) cout << x
#define DBGV(v) {cout << "["; FOR(i_, v) {DBG(i_); cout << ", ";} cout << "]" << endl; }

using namespace std;

typedef long long lint;
typedef vector<int> VI;
typedef vector<lint> VL;

int T;

void get_last(int n) {
	if (n == 0) {
		cout << "INSOMNIA";
		return;
	}

	unsigned int seen = 0;
	lint sum = 0;
	while (seen != 0x3ff) {
		sum += n;
		//cout << "KKK: " << sum << ".";
		lint digs = sum;
		while (digs > 0) {
			int d = digs % 10;
			digs = digs / 10;
			seen |= (1<<d);
		}
	}

	cout << sum;
}

int main(int argc, char *argv[])
{
	cin >> T;

	FORI(t, 0, T) {
		cout << "Case #" << (t+1) << ": ";

		int n;
		cin >> n;
		get_last(n);

		cout << endl;
	}


	return 0;
}
