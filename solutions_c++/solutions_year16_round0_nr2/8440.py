#include <stdio.h>
using namespace std;
int T,S;

char str[200];
void sol() {
	int slen;
	int i;

	char cur = str[0];
	int cnt = 1;
	for (i = 0; str[i]; i++) {
		if (str[i] != cur) {
			cnt++;
			cur = str[i];
		}
	}
	if (cur =='+') 
		cnt--;
	printf("%d\n", cnt);

}

int main() {
	scanf("%d\n", &T);

	for (int iter = 1; iter <= T; iter++) {
		printf("Case #%d: ", iter);
		scanf("%s", str);
		sol();
	}
}