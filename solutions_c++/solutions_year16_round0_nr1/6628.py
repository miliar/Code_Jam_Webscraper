#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>

using namespace std;

int check[11];


int main()
{
	int T;
	long long int onum;
	scanf("%d", &T);
	for (int t = 1;t <= T;t++) {
		scanf("%lld", &onum);
		for (int i = 0; i < 10;i++) check[i] = 0;
		long long int num, ans;
		bool iscom = false;
		if (onum == 0) printf("Case #%d: INSOMNIA\n", t);
		else {
			while (!iscom) {
				for (int i = 1;;i++) {
					ans = num = onum * i;
					while (num > 0) {
						check[num % 10] = 1;
						num /= 10;
					}
					bool ischeck = true;
					for (int j = 0;j < 10;j++) {
						if (check[j] == 0) ischeck = false;
					}
					if (ischeck) {
						printf("Case #%d: %lld\n", t, ans);
						iscom = true;
						break;
					}
				}
			}
		}
	}
	return 0;
}