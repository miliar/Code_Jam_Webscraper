#include<cstdio>
#include<fstream>
#include<iostream>
#include<string>
#include<math.h>
#define  DIGIT 7
using namespace std;

void main(int argc, char** argv) {
	int T;
	int test_case;
	freopen("A-large.in", "r", stdin);
	scanf("%d", &T);
	int i;
	int M;
	int N;
	int count;

	for (test_case = 1; test_case <= T; ++test_case) {
		cin >> N;
		char digit[10] = { 1,1,1,1,1,1,1,1,1,1 };
		if (!N) {
			cout << "Case #" << test_case << ": INSOMNIA" << endl;
			continue;
		}

		M = N;

		int result = 0;
		while (1) {
			int temp = M;
			count = 0;
			while (temp > 0) {
				count++;
				temp /= 10;
			}
			int a, c;
			c = M;
			for (i = 1; i < count+1; i++) { //N, 2N, 3N 각각에서 도는 for문 -- count만큼만 돈다
				if (i!=1) {
					if (!c) {
						digit[0] = 0;
						for (int j = 0; j < 10; j++) result += digit[j];

						if (!result) {
							printf("Case #%d: %d\n", test_case, M);
							break;
						}
					}
				}
				a = c / (int)pow(10, count - i);
				c = c % (int)pow(10, count - i);
				if (digit[a]) {
					digit[a] = 0;
					int result = 0;
					for (int j = 0; j < 10; j++) result += digit[j];

					if (!result) {
						printf("Case #%d: %d\n", test_case, M);
						break;
					}
				}
			}
			int result = 0;
			for (int j = 0; j < 10; j++) result += digit[j];
			if (!result) {
				break;
			}
			M += N;
		}
	}
}