
#include <iostream>

#define SIZE 101

using namespace std;

void filp(char* par, int num);

int main() {
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; i ++) {
		char pancake[SIZE];
		int cnt = 0;
		scanf("%s", pancake);
		for(int j = strlen(pancake) - 1; j >= 0; j--) {
			if(pancake[j] == '+') continue;
			filp(pancake, j);
			cnt++;
		}
		printf("Case #%d: %d\n", i, cnt);
	}

	return 0;
}

void filp(char* par, int num) {
	for(int i = 0; i <= num; i++) {
		if(par[i] == '+') par[i] = '-';
		else par[i] = '+';
	}
}