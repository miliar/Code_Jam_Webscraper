#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <list>
#include <cctype>
#include <cstdio>
#include <iterator>
#include <queue>

using namespace std;

typedef unsigned long long int ll;
vector <int> res;

void step (int m, map<int, int, std::greater<int> > p) {
	int x = p.begin()->first;
	int n = p.begin()->second;
	p.erase(p.begin());
	res.push_back(m+x);

	if(x <= 3)
		return;

	map<int, int, std::greater<int> > new_p = p;
	new_p[x/3] += n*2;
	new_p[(x+2)/3] += n;
	step(m + n*2, new_p);

	p[x/2] += n;
	p[(x+1)/2] += n;
	step(m + n, p);
}

int main() {
		
	int t;
	cin >> t;
	for(int k = 0; k < t; ++k) {
		res.clear();

		map <int, int, std::greater<int> > p;
		int d;
		cin >> d;
		for(int i = 0; i < d; ++i) {
			int val;
			cin >> val;
			++p[val];
		}

		step(0, p);

		cout << "Case #" << k+1 << ": " << *min_element(res.begin(), res.end()) << endl;
	}



	return 0;
}