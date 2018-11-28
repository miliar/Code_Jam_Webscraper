#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
using namespace std;

void solve(int caseNum) {
	int maxLevel = 0;
	char levels[1002] = {0};
	scanf("%d %s", &maxLevel, levels);

	int require = 0;
	int actual = 0;
	for (int level = 0; level <= maxLevel; level++) {
		int count = levels[level] - '0';
		int tmpRequire = level > actual ? (level - actual) : 0;
		require += tmpRequire;
		actual += count + tmpRequire;
	}
	cout << "Case #" << caseNum << ": " << require <<endl;
}

int main() {
	int cases = 0;
	cin >> cases;
	
	for(int caseNum = 1; caseNum <= cases; caseNum++) {
		solve(caseNum);
	}
}
