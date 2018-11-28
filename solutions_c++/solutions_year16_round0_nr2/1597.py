#define Revenge_of_the_Pancakes

#ifdef Revenge_of_the_Pancakes
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

char stack[100] = { 0 };

void flip(int idx) {
	for (int i = 0; i <= idx; i++) {
		if (stack[i] == '+')
			stack[i] = '-';
		else if (stack[i] == '-')
			stack[i] = '+';
	}
}

int count(int idx, bool f) {
	if (f) {
		if (idx == 0) {
			if (stack[idx] == '+')
				return 0;
			else if (stack[idx] == '-')
				return 1;
		}

		if (stack[idx] == '+')
			return 0 + count(idx - 1, true);
		else if (stack[idx] == '-') {
			flip(idx-1);
			return 1 + count(idx - 1, true);
		}
	}
	/*
	else {
		if (idx == 0) {
			if (stack[idx] == '+')
				return 0;
			else if (stack[idx] == '-')
				return 1;
		}

		if (stack[idx] == '+')
			return 1 + count(idx - 1, false);
		else if (stack[idx] == '-')
			return 0 + count(idx - 1, true);
	}
	*/
}

int main() {
	//freopen("in.txt","rt",stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		string str;
		getline(cin, str);
		//stack[100] = { 0 };
		memset(stack,0,sizeof(stack));
		int L = 0;
		bool new_count = true;
		char tmp;
		for (int j = 0; j < str.length(); j++) {
			if (new_count) {
				tmp = str[j];
				stack[L] = tmp;
				L++;
				new_count = false;
			}
			else {
				if (tmp == str[j]) {
					continue;
				}
				else {
					tmp = str[j];
					stack[L] = tmp;
					L++;
					new_count = false;
				}
			}
		}
		//memcpy(stack, str.c_str(), str.length());

		printf("Case #%d: %d\n", i, count(L-1, true));
		//printf("Case #%d: %d\n", i, count(str.length() - 1, true));
	}

	return 0;
}

#endif