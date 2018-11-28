#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

set<int> appears;

int solve(int num) {
	int num0 = num;
	while (appears.size() != 10) {
		int temp = num;
		while (temp != 0) {
			int find = temp % 10;
			appears.insert(find);
			temp = temp / 10;
		}
		num = num + num0;
	}
	return num - num0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		appears.clear();
		int num;
		cin >> num;
		int result;
		cout << "Case #" << i << ": ";
		if (num == 0)
			cout << "INSOMNIA" << endl;
		else
			cout << solve(num) << endl;
	}
	
	return 0;
}
