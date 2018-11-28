#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>

using namespace std;

int n;
int m;
char S[2222];
char R[2222];

void set(int l, int r, char *p)
{
	if (*p == 0) return;
	if (*p >= R[l]) {
		R[l-1] = *p;
		set(l-1, r, p+1);
	} else {
		R[r+1] = *p;
		set(l, r+1, p+1);
	}
}

void solve(int no)
{
	memset(R, 0, sizeof(R));
	int left = 1000;
	int right = 1000;
	// [left, right]
	scanf(" %s", S);
	R[left] = S[0];
	set(left, right, S+1);
	while (R[left-1])
		left--;
	printf("Case #%d: %s\n", no, R+left);
}

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; ++i)
		solve(i+1);
	return 0;
}
