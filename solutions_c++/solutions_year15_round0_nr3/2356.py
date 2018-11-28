#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <time.h>
using namespace std;
const int INF = 1e9;
const int N = 10001;
const int M[4][4] = {
	{ 1, 2, 3, 4 },
	{ 2, -1, 4, -3 },
	{ 3, -4, -1, 2 },
	{ 4, 3, -2, -1 }
};
int dp[N][N];

int get(char c){
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	if (c == 'k') return 4;
	throw 1;
}

int sign(int a){
	if (a > 0) return 1;
	else return -1;
}

int mul(int a, char b){
	return sign(a) * M[abs(a) - 1][get(b) - 1];
}

int mul(char a, int b){
	return sign(a) * M[get(a) - 1][abs(b) - 1];
}

bool solve(int X, int L, string s){
	string t;
	for (int i = 0; i < X; i++)
		t += s;
	if (t.length() < 3) return false;



	for (int i = 0; i < t.length(); i++){
		dp[i][i] = get(t[i]);
		for (int j = i + 1; j < t.length(); j++){
			dp[i][j] = mul(dp[i][j - 1], t[j]);
		}
	}


	for (int i = 0; i < t.length() - 2; i++)
		if (dp[0][i] == 2){
			for (int j = i + 1; j < t.length() - 1; j++){
				if (dp[i + 1][j] == 3 && dp[j + 1][t.length() - 1] == 4)
					return true;
			}
		}

	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++){
		int X, L;
		string s;
		cin >> L >> X >> s;
		
		printf("Case #%d: ", i);

		if (solve(X, L, s)){
			puts("YES");
		}
		else
			puts("NO");
	}
	return 0;
}