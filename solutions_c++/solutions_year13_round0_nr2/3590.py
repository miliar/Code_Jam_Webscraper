#include <iostream>
#include <fstream>
#include <vector>

#define FOR(i,n) for(int i = 0; i < (n); ++i)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;

int main() {
	ifstream fin("b2.in");
	ofstream fout("b2.out");
	int t;
	fin >> t;
	for (int tt = 1; tt <= t; ++tt) {
		int n,m;
		fin >> n >> m;
		VVI a(n,VI(m));
		FOR(i,n) FOR(j,m) fin >> a[i][j];
		VB rowDel(n,false);
		VB colDel(m,false);
		VB used(101,false);
		FOR(i,n) FOR(j,m) used[a[i][j]] = true;

		bool ok = true;
		FOR(k,101) if (used[k]) {
			FOR(i,n) if (!rowDel[i]) {
				bool del = true;
				FOR(j,m) if (!colDel[j]) {
					if (a[i][j] < k) { ok = false; goto over; }
					else if (a[i][j] > k) { del = false; break; }
				}
				if (del) rowDel[i] = true;
			}
			FOR(j,m) if (!colDel[j]) {
				bool del = true;
				FOR(i,n) if (!rowDel[i]) {
					if (a[i][j] < k) { ok = false; goto over; }
					else if (a[i][j] > k) { del = false; break; }
				}
				if (del) colDel[j] = true;
			}
		}
over:
		fout << "Case #" << tt << ": ";
		fout << (ok ? "YES" : "NO");
		fout << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
