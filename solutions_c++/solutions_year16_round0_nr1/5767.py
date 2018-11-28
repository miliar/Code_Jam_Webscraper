#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int casenum, N;
	bool occur[10];

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin >> casenum;
	for(int i = 1; i <= casenum; i++) {
		cin >> N;
		if (N == 0) {printf("Case #%d: INSOMNIA\n", i); continue;}
		memset(occur, false, sizeof(occur));
		int cnt = 1, num = 0;
		while(num < 10) {
			int temp = cnt * N;
			while(temp > 0) {
				if(occur[temp%10] == false) { num++; occur[temp%10] = true;}
				temp /= 10;
			}
			cnt += 1;
		}
		printf("Case #%d: %d\n", i, (cnt - 1) * N);
	}

	return 0;
}