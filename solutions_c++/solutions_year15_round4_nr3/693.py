#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <map>
using namespace std;
string line[30];
map<string, int> mp;
int t, n;

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		scanf("%d", &n);
		getline(cin, line[0]);
		for (int i = 0; i < n; ++i)
			getline(cin, line[i]);
		mp.clear();
		for (int i = 0; i < n; ++i) {
			stringstream ss(line[i]);
			string str;
			while (ss >> str)
				mp[str] = 0;
		}
		int k = 0;
		for (map<string, int>::iterator mpi = mp.begin(); mpi != mp.end(); ++mpi) {
			mpi->second = k;
			++k;
		}
		bitset<3000> v[30];
		for (int i = 0; i < n; ++i) {
			v[i].reset();
			stringstream ss(line[i]);
			string str;
			while (ss >> str)
				v[i].set(mp[str], 1);
		}
		int ans = 0x3f3f3f3f;
		bitset<3000> b[2];
		for (int i = 2; i < (1 << n); i += 4) {
			b[0].reset();
			b[1].reset();
			for (int j = 0; j < n; ++j)
				if (i & (1 << j))
					b[1] |= v[j];
				else b[0] |= v[j];
			bitset<3000> bb = b[0] & b[1];
//			cout << i << " " << bb.count() << endl;
			ans = min(ans, (int)bb.count());
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
