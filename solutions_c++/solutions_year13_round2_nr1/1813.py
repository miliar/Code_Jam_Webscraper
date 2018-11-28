#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> v;

int f(long long a, long long n, int i, int m) {
	int moves = m;
	for (; i<n; ++i) {
		if (a>v[i]) {
			a += v[i];
			//cout << "Zjadam " << v[i] << " mam " << a << endl;
		} else {
			long long diff = v[i]+1-a;
			if (diff < a) {
				//cout << "Dodaje " << a-1 << endl;
				a += a-1;
				a += v[i];
				++moves;
			} else {
				//cout << "Rekurencja: " << endl;
				int remMoves = moves + n-i; //remove all from i
				//cout << "  Usun reszte to ruchow: " << remMoves << endl;
				while (a <= v[i] && moves<remMoves) {
					//cout << "Dodaje w petli " << a-1 << " mam " << a << endl;
					a += a-1;
					++moves;
				}
				moves = f(a,n,i,moves);
				//cout << "  Rekurencja zwrocila: " << moves << endl;
				return (moves<remMoves) ? moves : remMoves;
			}
		}
	}
	return moves;
}

int main() {
	int t;
	cin >> t;
	for (int ti=0; ti<t; ++ti) {
		long long a, n, tmp;
		cin >> a >> n;

		v.clear();
		for (int i=0; i<n; ++i) {
			cin >> tmp;
			v.push_back(tmp);
		}

		if (a==1) {
			cout << "Case #" << ti+1 << ": " << n << endl;
			continue;
		}

		sort(v.begin(), v.end());

		int moves=f(a,n,0,0);
		cout << "Case #" << ti+1 << ": " << moves << endl;
	}

	//system("PAUSE");
	return 0;
}