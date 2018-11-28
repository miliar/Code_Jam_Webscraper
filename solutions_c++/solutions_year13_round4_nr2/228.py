#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int t;
int n;
long long p;
fstream in, out;

vector<long long> expcache;

long long must_win(int num, long long prize) {
	if (num == 0) {
		return 1;
	} else if (prize <= expcache[num - 1]) {
		return 1;
	} else {
		long long ans = must_win(num - 1, prize - expcache[num - 1]);
		return 2 * ans + 1;
	}
}

long long could_win(int num, long long prize) {
	long long must = must_win(num, expcache[num] - prize);
	return expcache[num] - must;
}

int main() {
	in.open("B-large.in", fstream::in);
	out.open("probb-large.out", fstream::out);
	
	long long ret = 1;
	for (int i = 0; i < 52; i++) {
		expcache.push_back(ret);
		ret *= 2;
	}

	in >> t;
    for (int i = 0; i < t; i++) {
		in >> n >> p;
		
		long long ans1 = must_win(n, p) - 1;
		long long ans2 = could_win(n, p) - 1;
		
		if (p == expcache[n]) {
			ans1 = expcache[n] - 1;
			ans2 = expcache[n] - 1;
		}

		out << "Case #" << i + 1 << ": " << ans1 << " " << ans2 << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
