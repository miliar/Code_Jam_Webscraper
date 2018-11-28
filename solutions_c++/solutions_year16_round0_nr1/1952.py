#include<iostream>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<fstream>
using namespace std;
int mp[10];
bool seeNumbers(int n) {
	while (n > 0) {
		mp[n % 10] = 1;
		n /= 10;

	}
	int cnt = 0;
	for (int i = 0; i < 10; ++i) {
		cnt += mp[i];
	}
	return cnt == 10;
}
int main() {
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int t, n;
	in >> t;
	for (int z = 1; z <= t; ++z) {
		in >> n;
		memset(mp, 0, sizeof mp);
		if (n == 0) {
			out << "Case #" << z << ": INSOMNIA" << endl;
			continue;
		}
		int looper = 1;
		while (!seeNumbers(n*looper)) {
			looper++;
		}
		out << "Case #" << z << ": " << looper*n << endl;
	}
	return 0;
}