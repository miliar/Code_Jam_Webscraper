#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;
typedef long long ll;
int f[26], res[26], n;
string x[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
void take(char e, int d){
	while (f[e - 'A'] > 0){
		++res[d];
		for (int i = 0; i < x[d].size(); ++i)
			--f[x[d][i] - 'A'];
	}
}
int main(){
	freopen("src.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		string s;
		cin >> s;
		memset(f, 0, sizeof(f));
		memset(res, 0, sizeof(res));
		for (int i = 0; i < s.size(); ++i)
			++f[s[i] - 'A'];
		take('Z', 0);
		take('X', 6);
		take('W', 2);
		take('U', 4);
		take('O', 1);
		take('F', 5);
		take('G', 8);
		take('R', 3);
		take('V', 7);
		take('I', 9);
		printf("Case #%d: ", k);
		for (int i = 0; i < 26;++i)
		while (res[i]){
			printf("%d", i);
			--res[i];
		}
		puts("");
	}
}

// "THREE", , "SEVEN", , "NINE"