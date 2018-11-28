#include<cstdio>
#include<stdlib.h>
#include<string.h>
int Test_num[101];
int Answer[10] = { 0 };
int index = 0;
void Test();
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("outputA.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &Test_num[i]);
		Test();
		index++;
	}

	return 0;
}
void Test() {
	int check;
	int print_num;
	int real;
	int good = 10;
	int check_num = 0;
	if (Test_num[index] == 0) {
		printf("Case #%d: INSOMNIA\n",index+1);
		return;
	}
	real = Test_num[index];
	for (int k = 2; ; k++) {
		print_num = real;
		check_num = real;
		while (check_num > 0) {
			check = check_num % 10;
			if (Answer[check] == 0) {
				Answer[check] = 1;
				good--;
				if (good == 0) {
					printf("Case #%d: %d\n", index+1 , print_num);
					memset(Answer, 0, sizeof(Answer));
					return;
				}
			}
			check_num = check_num / 10;
		}
		real = Test_num[index] * k;
	}
	memset(Answer, 0, sizeof(Answer));
	printf("Case #%d: INSOMNIA\n", index + 1);
	return;

}