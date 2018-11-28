#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<bitset>
#include <cstdio>
using namespace std;
int main(void) {
	int totalCase, cases;
	int n, c, s;
	int i,j,k,ans,tocheck;
	unsigned long long int upto;
	ifstream cin("s.in");
	ofstream cout("s.out");
	cin >> totalCase;
	for (cases = 1; cases <= totalCase; cases++) {
		cin >> n >> c >> s;
		c--;
		cout << "Case #" << cases << ": ";
		if (n == 1) {
			cout << "1 " << endl;
			continue;
		}
		ans = n - c;
		if (ans < 1) {
			ans = 1;
			c = n - 1;
		}
		if (ans > s) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}/////////////////////////////////////
		upto = 1;
		tocheck = n-2;
		for (; c > 1; c--, tocheck--) {
			upto = upto*n - tocheck;
		}
		upto *= n;
		for (i = 0; i < ans; i++, upto--)cout << upto << " ";
		cout << endl;
	}////////////////////////////////////////case
	system("pause");
	return 0;
}
