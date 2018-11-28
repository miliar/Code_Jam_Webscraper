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
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\B-large.in", "r", stdin);
	//freopen_s(&file, "C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t, first, second, temp, c, ans, atable[4][4], btable[4][4];

	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> first;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> atable[j][k];
		cin >> second;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> btable[j][k];
		c = 0;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (atable[first-1][j] == btable[second-1][k]) {
					c++;
					ans = atable[first-1][j];
				}
		if (c == 0)
			cout << "Case #" << i << ": Volunteer cheated!\n";
		else if (c == 1)
			cout << "Case #" << i << ": " << ans << endl;
		else
			cout << "Case #" << i << ": Bad magician!\n";
	}

	return 0;
}