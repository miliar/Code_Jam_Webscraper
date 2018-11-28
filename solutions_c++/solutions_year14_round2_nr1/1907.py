#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

int N;
string strs[100];
string strCpys[100];
char buffer[100];
int pointer[100];
int charCount[100];

void updateCount()
{
	for (int i = 0; i < N; i++) {
		int j;
		for (j = pointer[i]+1; strs[i][j] == strs[i][pointer[i]]; j++) {}
		charCount[i] = j - pointer[i];
	}
}

void nextPtr()
{
	for (int i = 0; i < N; i++) {
		pointer[i] += charCount[i];
	}
	updateCount();
}

int avg()
{
	int ret = 0;
	for (int i = 0; i < N; i++) {
		ret += charCount[i];
	}
	ret /= N;
	return ret;
}

int totDeviation()
{
	int average = avg();
	int moves = 0;
	for (int i = 0; i < N; i++) {
		int temp = charCount[i] - average;
		if (temp < 0) temp *= -1;
		moves += temp;
	}
	return moves;
}

int solve()
{
	int ans = 0;
	fill(pointer, pointer+N, 0);
	updateCount();
	while ( strs[0][pointer[0]] != '\0' ) {
		ans += totDeviation();
		nextPtr();
	}
	return ans;
}


int main()
{
	int T; cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> buffer;
			strs[i] = buffer;
			unique(buffer, buffer+strlen(buffer)+1);
			strCpys[i] = buffer;
		}
		bool works = true;
		for (int i = 1; i < N; i++) {
			if (strCpys[i] != strCpys[0]) {
				works = false;
				break;
			}
		}
		printf("Case #%i: ", cas);
		if (works)
			printf("%i\n", solve());
		else
			printf("Fegla Won\n");
	}
	return 0;
}
