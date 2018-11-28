#include <iostream>
#include <cstdio>
#include <cstring>
#include <deque>
using namespace std;

char input[1000];

void calculate(char * input, int len) {
	deque<char> result = deque<char>(len);
	result.push_front(input[0]);
	for (int i=1; i<len; i++) {
		if (result.front() <= input[i]) {
			result.push_front(input[i]);
		} else {
			result.push_back(input[i]);
		}
	}
	for (deque<char>::iterator it = result.begin(); it!=result.end(); it++) {
		printf("%c", *it);
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d\n", &T);
	for (int i=1; i<=T; i++) {
		scanf("%s\n", input);
		int len = strlen(input);
		printf("Case #%d: ", i);
		calculate(input, len);
	}
}
