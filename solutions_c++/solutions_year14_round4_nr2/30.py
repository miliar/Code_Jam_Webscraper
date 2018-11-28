#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int n;
vector<int> a;
map<int, int> id;

void Load()
{
	cin >> n;
	id.clear();
	a.clear();
	a.resize(n);
	vector<int> b;
	int i;
	for (i = 0; i < n; i++) {
		cin >> a[i];
		b.push_back(a[i]);
	}
	sort(b.begin(), b.end());
	for (i = 0; i < n; i++) {
		id[b[i]] = i;
	}

	for (i = 0; i < n; i++) {
		a[i] = id[a[i]];
	//	cerr << a[i] << ' ';
	}
	//cerr << "\n";

}

void Solve()
{
	vector < int > b;
	vector < int > p;
	vector < int > ainv;
	ainv.resize(n);
	p.resize(n);
	int i;
	int ans = n*n;
	for (i = 0; i < n; i++)
		ainv[a[i]] = i;
	for (i = 0; i < n; i++)
		b.push_back(i);
	do {
		bool good = true;
		bool nseen = false;
		for (i = 0; i < n-1; i++) {
			//cerr << b[i] << " " << nseen << " " << good << "\n";
			if (b[i] == n-1) nseen = true;
			if (!nseen && b[i] > b[i+1]) good = false;
			if (nseen && b[i] < b[i+1]) good = false;
		}
		if (!good) {
			//cerr << "bad \n";
		  continue;
		}
		for (i = 0; i < n; i++) {
			p[ainv[b[i]]] = i;

		}
/*		for (i = 0; i < n; i++) {
			cerr << p[i] << " ";
		}
		cerr << ": ";*/
		int cur = 0;
		int j;
		for (i = 0; i < n; i++) {
			for (j = 0; j < i; j++) {
				if (p[j] > p[i]) cur++;
			}
		}
		//cerr << cur << "\n";
		if (cur < ans) ans = cur;
	} while (next_permutation(b.begin(), b.end()));
	cout << ans << "\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
