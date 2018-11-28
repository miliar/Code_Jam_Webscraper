#include<stdio.h>

void process() {

	int cnt = 0;
	char str[105] = { 0, };
	scanf("%s", str);
	int i = 1;
	

	while (str[i]) {

		if (str[i] != str[i - 1])
			cnt++;
		i++;
	}
	if (str[i-1] == '-')
		cnt++;
	printf("%d\n",cnt);

}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int testcase; scanf("%d", &testcase);


	for (int i = 1; i <= testcase; i++) {
		printf("Case #%d: ", i);
		process();
		
	}


	return 0;
}