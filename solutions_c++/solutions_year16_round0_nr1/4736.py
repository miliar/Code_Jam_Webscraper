#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<map>
using namespace std;

int main() {
	//FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	//FILE *fout = freopen("A-small-attempt0.out", "w", stdout);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		if (n == 0)
		{
			cout << "Case #" << t << ": "<<"INSOMNIA";
			cout<<endl;
			continue;
		}

		map<int, int> mp;
		int n1;
		int m;
		int digit;
		int k = 1;
		while (mp.size() < 10)
		{
			n1 = n*k;
			m = n1;
			while (m)
			{
				digit = m % 10;
				mp[digit] = digit;
				m /= 10;
			}
			k++;
		}
		
		cout << "Case #" << t << ": ";
		cout << n1 << endl;
	}
	exit(0);
}