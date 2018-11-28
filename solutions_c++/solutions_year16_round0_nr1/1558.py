#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
int main(void) {
	int totalCase, cases;
	int i, j, k, len;
	long long tem, n;
	bool done[10];
	string s;
	ifstream cin("l.in");
	ofstream cout("l.out");
	cin >> totalCase;
	for (cases = 1; cases <= totalCase; cases++) {
		cin >> n;
		cout << "Case #" << cases << ": ";
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		for (i = 0; i<10; i++)done[i] = false;
		tem = n;
		while (1) {
			s = to_string(tem);
			len = s.length();
			for (j = 0; j<len; j++) {
				k = s[j] - '0';
				done[k] = true;
			}
			if (done[0] && done[1] && done[2] && done[3] && done[4] && done[5] && done[6] && done[7] && done[8] && done[9])break;
			tem += n;
		}
		cout << tem << endl;
	}
	system("pause");
	return 0;
}
