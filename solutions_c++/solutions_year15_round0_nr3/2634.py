#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
using namespace std;

int L, X;
int list[100001];
const int board[5][5] = {
	0, 0, 0, 0, 0,
	0, 1, 2, 3, 4,
	0, 2, -1, 4, -3,
	0, 3, -4, -1, 2,
	0, 4, 3, -2, -1};
int memo[10000][10000];

int Solve(int i, int j) {
	if (i == j)
		return list[i];
	else if (j == i+1)
		return board[list[i]][list[j]];
	int &ret = memo[i][j];
	if (ret != 0) return ret;
	int head = board[list[i]][list[i+1]];
	int tail = Solve(i+2,j);
	int sign = head * tail > 0 ? 1 : -1;

	return ret = sign * board[abs(head)][abs(tail)];
}

int main() {
	int testNum;
	cin >> testNum;
	int caseNum = 0;
	while (++caseNum <= testNum) {
		cin >> L >> X;
		memset(memo, 0, sizeof(memo));
		cin.get();
		for (int i=0; i<L; ++i) {
			char ch = cin.get();
			if (ch == 'i')
				list[i] = 2;
			else if (ch == 'j')
				list[i] = 3;
			else list[i] = 4;
		}
		for (int i=L; i<L*X; ++i)
			list[i] = list[i%L];

		bool ret = false;
		for (int i=1; i<L*X-1; ++i) {
			for (int j=i+1; j<L*X; ++j)
				if (Solve(0, i-1) == 2 && Solve(i, j-1) == 3 && Solve(j, L*X-1) == 4) {
					ret = true;
					break;
				}
			if (ret)
				break;
		}
		if (ret)
			printf("Case #%d: YES\n",caseNum);
		else
			printf("Case #%d: NO\n",caseNum);
	}
	return 0;
}
