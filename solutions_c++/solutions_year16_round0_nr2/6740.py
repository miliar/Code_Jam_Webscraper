#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

#define swap(a,b) ((a)^=(b)^=(a)^=(b));

using namespace std;

int i;

void func() {
	string t;
	int a;
	int ans=0;
	getline(cin, t);
	a = t.length();
	for (int l = 0; l < a-1; l++) {
		if (t[l] != t[l + 1]) ans++;
	}
	if (t[a-1] == '-') ans++;
	printf("Case #%d: %d\n", i+1, ans);
}

int main() {

	int testcase;

	scanf("%d", &testcase);
	getchar();
	for (i = 0; i < testcase; i++) {
		func();
	}

	return 0;

}