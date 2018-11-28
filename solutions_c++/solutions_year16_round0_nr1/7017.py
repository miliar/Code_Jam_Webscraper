#include <iostream>
using namespace std;
int arr;

void func(int a) {
	if (a == 0)
		return;
	else {
		func(a / 10);
		if (a % 10 >= 0)
			arr |= 1 << (a % 10);
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("Ans.txt", "w", stdout);
	int t; scanf("%d", &t);
	int Case = 1;
	while (t--) {
		int num; scanf("%d", &num);
		int count = 1, prev_arr = 0, flag = 0;
		func(num);
		prev_arr = arr;
		while (1) {
			func(num * (++count));
			if (prev_arr == arr && count > 100) {
				printf("Case #%d: INSOMNIA\n", Case);
				flag = 1;
				break;
			}	
			if (arr == (1 << 10) - 1)
				break;
			prev_arr = arr;
		}
		if (flag == 0)
			printf("Case #%d: %d\n", Case, num * count);
		arr = 0;
		Case++;
	}
}