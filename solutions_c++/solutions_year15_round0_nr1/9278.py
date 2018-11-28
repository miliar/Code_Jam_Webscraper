#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <queue>
#include <algorithm>
#include <map>
#include <set>

using namespace std;



int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	//std::ifstream cin("/home/shrubb/Projects/ClionProjects/Round278/input.txt");
	//std::ofstream cout("/home/shrubb/Projects/ClionProjects/Round278/output.txt");

	char s[1005];
	int tests;

	cin >> tests;

	for (int i = 0; i < tests; ++i) {
		int len;
		cin >> len; ++len;
		cin >> s;

		int ans = 0;
		int standing = 0;
		for (int j = 0; j < len; ++j) {
			if (standing < j && s[j] != '0') {
				ans += j - standing;
				standing = j;
			}
			standing += s[j] - '0';
		}

		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}