#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string.h>
#include <utility>
#include <vector>
using namespace std;

FILE * file;

int main() {
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\input.txt", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\output.txt", "w", stdout);
	freopen_s(&file, "C:\\Users\\wayne\\Downloads\\D-small-attempt3.in", "r", stdin);
	freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Small-output.out", "w", stdout);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\D-large.in", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t, num, cheat, notcheat;
	double n[1000], m[1000];

	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> num;
		for (int j = 0; j < num; j++)
			cin >> n[j];
		for (int j = 0; j < num; j++)
			cin >> m[j];
		sort(n, n + num);
		sort(m, m + num);
		notcheat = -1;
		for (int j = 0; j < num; j++) {
			notcheat = lower_bound(m + notcheat + 1, m + num, n[j]) - m;
			if (notcheat == num) {
				notcheat = num - j;
				break;
			}
			if (notcheat == num - 1) {
				notcheat = num - j - 1;
				break;
			}
		}
		cheat = num;
		for (int j = 0, k = 0; j < num; j++) {
			if (n[j] <= m[k])
				cheat--;
			else
				k++;
		}

		cout << "Case #" << i << ": " << cheat << " " << notcheat << endl;
	}

	return 0;
}