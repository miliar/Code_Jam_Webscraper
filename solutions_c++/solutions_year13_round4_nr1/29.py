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


int n, m;
vector<int> o, e, p;
vector<pair<int, int> > ev;
long long mod = 1000002013;
long long total;

void Load()
{
	cin >> n >> m;
	int i;
	o.resize(m);
	e.resize(m);
	p.resize(m);
	ev.clear();
	total = 0;
	for (i = 0; i < m; i++)
	{
		cin >> o[i] >> e[i] >> p[i];
		long long l = e[i] - o[i];
		long long cst = (n*(l) - (l)*(l-1)/2) % mod;
		total += (cst * p[i]);
		total %= mod;
		ev.push_back(make_pair(o[i], -p[i]));
		ev.push_back(make_pair(e[i], +p[i]));
	}
//	cerr << total << "\n";
}

void Calc(int b, int e, int p) {
	long long l = e - b;
	long long cst =  (n*(l) - l*(l-1)/2) % mod;
	total -= (cst * p) % mod;
	if (total < 0) total += mod;
}

void Solve()
{
	int i, j;
	sort(ev.begin(), ev.end());
	vector <pair<int, int> > stack;
	for (i = 0; i < ev.size(); i++) {
		pair<int, int> cur = ev[i];
		if (cur.second < 0) {
			cur.second = -cur.second;	
			stack.push_back(cur);
		} else {
			while (cur.second > 0) {
				if (stack.back().second > cur.second) {
					Calc(stack.back().first, cur.first, cur.second);
					stack.back().second -= cur.second;
					cur.second = 0;
				} else {
					Calc(stack.back().first, cur.first, stack.back().second);
					cur.second -= stack.back().second;
					stack.pop_back();
				}
			}
		}
	}
	cout << total << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
