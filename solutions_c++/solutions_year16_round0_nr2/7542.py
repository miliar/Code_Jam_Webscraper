//============================================================================
// Name        : codeJam_B.cpp
// Author      : wufy
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	char inStr[110];
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%s", inStr);
		int inStrLen = strlen(inStr);
		int ans = 0; // inStr[0] == '+' ? 0 : 1;
		for (int i = 1; i < inStrLen; i++) {
			if (inStr[i] != inStr[i - 1])
				ans ++;
		}
		if (inStr[inStrLen - 1] == '-')
			ans ++;

		printf("Case #%d: ", cas);
		printf("%d\n", ans);
	}
	return 0;
}
