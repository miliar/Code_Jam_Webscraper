#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define MAX 128
int INF = 9876543210;
char pan[100];
bool p[100];
int N;

void flip(bool* str, int num) {
	bool temp;
	if (num % 2 == 1)
		str[num/2] = !str[num/2];
	for(int i = 0; i < num/2; i++) {
		temp = str[i];
		str[i] = !str[num-i-1];
		str[num-i-1] = !temp;
	}
}

bool check(bool* str) {
	forn(i, N) {
		if(!str[i])
			break;
		else if (i == (N-1))
			return true;
	}
	return false;
}

/*
int opt(bool* sec, int size, int f) {
	bool temp[100];
	int m = INF;
	memcpy(temp, sec, size);

	for(int i = 1; i < N+1; i++) {
		flip(temp, i);
		if (check(temp))
			return 1;
		flip(temp, i);
	}

	return m;
}
*/

int opt(bool* sec, int size, int start) {
	bool temp[100];
	int m = INF;
	memcpy(temp, sec, size);

	for(int i = start; i < N+1; i++) {
		flip(temp, i);
		if (check(temp))
			return 1;
		flip(temp, i);
	}

	for(int i = start; i < N+1; i++) {
		flip(temp, i);
		m = min(m, opt(temp, size, i+1) + 1);
		flip(temp, i);
	}

	return m;
}

int solve() {
	int nf = 0;
	cin >> pan;
	N = strlen(pan);
	forn(i, N)
		pan[i] == '+' ? p[i] = true : p[i] = false;
	if (check(p))
		return nf;
	
	return opt(p, sizeof(p), 1);
}

int main()
{
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
		printf("Case #%d: %d\n", i+1, solve());
	}

	return 0;
}
