#include <cstdio>
#include <gmpxx.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

char mount[1000];
vector<mpz_class> res;

mpz_class create(const char* c, int d)
{
	mount[d] = 0;
	stringstream str;
	str << mount << c;
	reverse(mount, mount+d);
	str << mount;
	reverse(mount, mount+d);
	mpz_class n;
	str >> n;
	return n*n;
}

void gen(int p, int d, int l)
{
	if (d >= 10 || l*2 > 101) return;
	if (d+4 < 10) res.push_back(create("2", p));
	if (d+1 < 10) res.push_back(create("1", p));
	res.push_back(create("0", p));
	res.push_back(create("", p));
	mount[p] = '0'; gen(p+1, d, l+1);
	mount[p] = '1'; gen(p+1, d+2, l+1);
	mount[p] = '2'; gen(p+1, d+8, l+1);
}

void pre()
{
	res.push_back(1); res.push_back(4); res.push_back(9);
	mount[0] = '1'; gen(1, 2, 0);
	mount[0] = '2'; gen(1, 8, 0);
}

int main()
{
	pre();
	sort(res.begin(), res.end());
	//for (int i = 0; i < res.size(); ++i)
	//	cout << res[i] << endl;
	//cout << res.size() << endl;
	
	int t;
	ios_base::sync_with_stdio(false);
	cin >> t;
	
	for (int q = 1; q <= t; ++q)
	{
		mpz_class a, b;
		cin >> a;
		--a;
		int ra = upper_bound(res.begin(), res.end(), a)-res.begin();
		cin >> b;
		int rb = upper_bound(res.begin(), res.end(), b)-res.begin();
		cout << "Case #" << q << ": " << rb-ra << endl;
	}
}

