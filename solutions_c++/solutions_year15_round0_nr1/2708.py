#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int S_max;
		string line;
		cin >> S_max >> line;
		int req = 0, standing = 0;
		for (int i = 0; i <= S_max; i++) {
			int value = line[i] - '0';
			if (value == 0)
				continue;
			if (i <= standing)
				standing += value;
			else
			{
				req += i - standing;
				standing += value + i - standing;
			}
		}
		printf("Case #%d: %d\n", t + 1, req);
	}
	return 0;
}