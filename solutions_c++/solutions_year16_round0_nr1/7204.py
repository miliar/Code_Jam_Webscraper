#include <iostream>
#include <stdio.h>
#define MAX 1000006
using namespace std;


long long int out[MAX];
int found[10];
void clear_found() {
	for (int i = 0; i<10; i++) {
		found[i] = 0;
	}
}

int check_found() {
	for (int i = 0; i<10; i++) {
		if (!found[i]) {
			return 0;
		}
	}
	return 1;
}

void add_found(int i) {
	while(i>0) {
		found[i%10] = 1;
		i = i/10;
	}
}

int main() {
	int n, i, j;
	for (i=1; i<MAX; i++) {
		clear_found();

		j = 0;
		while(!check_found()) {
			j += i;
			add_found(j);
		}
		out[i] = j;
	}
	scanf("%d", &n);
	j = 1;
	while(n--) {
		scanf("%d", &i);
		if (i == 0) {
			printf("Case #%d: INSOMNIA\n", j);
		} else {
			printf("Case #%d: %lld\n", j, out[i]);
		}
		j++;
	}


	return 0;
}
