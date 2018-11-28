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

FILE *file;

int main() {
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\input.txt", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\output.txt", "w", stdout);
	freopen_s(&file, "C:\\Users\\wayne\\Downloads\\A-small-attempt1.in", "r", stdin);
	freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Small-output.out", "w", stdout);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\A-large.in", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t, a, b, temp, c, num, atable[4], btable[4];

	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> a;
		for (int j = 1; j <= 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (j == a)
					cin >> atable[k];
				else
					cin >> temp;
			}
		}
		cin >> b;
		for (int j = 1; j <= 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (j == b)
					cin >> btable[k];
				else
					cin >> temp;
			}
		}
		c = 0;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (atable[j] == btable[k]) {
					c++;
					num = atable[j];
				}
			}
		}
		if (c == 0)
			cout << "Case #" << i << ": Volunteer cheated!\n";
		else if (c == 1)
			cout << "Case #" << i << ": " << num << endl;
		else
			cout << "Case #" << i << ": Bad magician!\n";
	}

	return 0;
}