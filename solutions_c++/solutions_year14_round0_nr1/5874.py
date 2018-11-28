#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <iomanip>
#include <locale>
#include <sstream>
#include <vector>
using namespace std;

int ans[2],board[2][4][4];

string answer() {
	for (int it = 0; it < 2; it++) {
		scanf("%d", &ans[it]);
		ans[it]--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) scanf("%d", &board[it][i][j]);
	}
	
	int ret = 0;
	for (int choice = 1; choice <= 16; choice++) {
		bool valid0 = false;
		for (int i = 0; i < 4; i++) if (board[0][ans[0]][i] == choice) valid0 = true;
		bool valid1 = false;
		for (int i = 0; i < 4; i++) if (board[1][ans[1]][i] == choice) valid1 = true;
		if (!valid0 || !valid1) continue;
		// cout << choice << endl;
		if (ret > 0) return "Bad magician!";
		ret = choice;
	}
	if (ret == 0) return "Volunteer cheated!";
	ostringstream number;
	number << ret;
	return number.str();
}

int main() {
	int T;
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) cout << "Case #" << it << ": " << answer() << endl;
}