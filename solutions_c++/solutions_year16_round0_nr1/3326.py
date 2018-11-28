#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll f(ll N) {
	ll st = 0;
	ll NN = 0;
	while(st != ((1<<10)-1)) {
		NN += N;
		ll n = NN;
		while(n) {
			st |= 1 << (n % 10);
			n /= 10;
		}
	}
	return NN;
}

int main() {
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int T; fin >> T;
	for(int cs = 1; cs <= T; cs++) {
		int N; fin >> N;
		fout << "Case #" << cs << ": ";
		if(N) fout << f(N) << "\n";
		else fout << "INSOMNIA\n";
	}
}
