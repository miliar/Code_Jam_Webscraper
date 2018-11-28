//============================================================================
// Name        : codeJam_A.cpp
// Author      : wufy
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;



long long getAns(long long N)
{
	int sourceN = N;
	bool viewArr[11] = {false};
	int num = 0;
	while (num < 10) {
		long long temp = N;
		while(temp)
		{
			int pos = temp % 10;
			if (!viewArr[pos]) {
				viewArr[pos] = true;
				num ++;
			}
			temp /= 10;
		}
		if (num > 9)
			break;

		N = N + sourceN;
	}
	return N;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	long long N;
	scanf("%d",&T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%lld",&N);
		printf("Case #%d: ", cas);
		if(N == 0)
			printf("INSOMNIA\n");
		else
			printf("%lld\n", getAns(N));
	}

//	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
