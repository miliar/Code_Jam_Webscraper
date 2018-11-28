#include <iostream> 
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stack>
#include <deque>
#include <numeric>
#include <ctime>

using namespace std;

typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-10;

bool isOk(int q) {
	int i=0;
	//int a = 1;
	while ( q > 1) {
		if (q % 2 != 0)
			return false;
		q /= 2;
	}
	return true;
}

int log(int q) {
	int i=0;
	int a = 1;
	while ( a < q) {
		a*= 2;
		i++;
	}
	return i;
}

set<int> deg;

int solve(int p, int q) {
	if (p == 0) return 45;
	while (p % 2 == 0) {
		p/= 2;
		q/= 2;
	}
	if (p == 1 && q == 2) return 1;
	if (p == 0 && q == 2) return 45;
	if (p == 1 && q == 1) return 0;
	set<int>::iterator it;
	it = deg.upper_bound(p);
	int k = *it;
	return min(solve(*it/2, q/2), solve(p - *it/2, q/2)) + 1;
}

int main()
{
	int t;
	int p, q;
	//ifstream fin("A-large.in");
	//ofstream fout("A-large.out");
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	//ifstream fin("a.in");
	//ofstream fout("a.out");
	fin >> t;
	

	for (int i=1; i < 1025; i*=2) {
		deg.insert(i);
	}
	for (int ti = 1; ti <= t; ti++) {
		string s;
		p = 0;
		q = 0;
		fin >> s;
		int i=0;
		while (s[i] != '/') {
			p *= 10;
			p += (int) (s[i] - '0');
			i++;
		}
		i++;
		while (i < s.length()) {
			q *= 10;
			q += (int) (s[i] - '0');
			i++;
		}
		//i++;
		int ans;
		if (isOk(q)) {
			//int l = log(q);
			//if ( p * 2 < q) {
			ans = solve(p, q);
			fout << "Case #" << ti <<": " << ans <<endl;
		}
		else {
			fout << "Case #" << ti <<": " << "impossible" <<endl;

		}

		
		

	}

	fout.close();
	return 0;
}



