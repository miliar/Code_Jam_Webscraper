#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
int t, tt;
string a, jawab;
int main() {
	ios_base::sync_with_stdio(false);
	cin >> t;
	for (int q = 1; q <= t; q++) {
		cin >> a;
		jawab = "";
		tt = a.length();
		for (int i = 0; i < tt; i++) {
			if (i == 0) jawab = a[i] + jawab;
			else if (a[i] >= jawab[0]) jawab = a[i] + jawab;
			else jawab = jawab + a[i];
		}
		cout <<"Case #"<<q<<": "<<jawab << endl;
	}
}