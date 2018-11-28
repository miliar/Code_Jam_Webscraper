#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

void switch_txt(string &str, int end) {
	for (int i=0; i<end; i++)
		str[i] = (str[i] == '+' ? '-' : '+');
}

int run() {
	string str;
	cin >> str;
	
	int cnt = 0;
	bool different = true;
	
	while (different) {
		different = false;
		
		for (int i=1; i<str.length(); i++) {
			if (str[i] != str[i-1]) {
				switch_txt(str, i);
				cnt++;
				different = true;
			}
		}
	}
	
	if (str[0] == '-') cnt++;
	return cnt;
}

int main() {
	int testCase;
	scanf("%d", &testCase);
	
	for (int t=1; t<=testCase; t++) {
		int ret = run();
		printf("Case #%d: %d\n", t, ret);
	}
}
