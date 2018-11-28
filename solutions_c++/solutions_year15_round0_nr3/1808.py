#pragma comment(linker, "/STACK:512000000")
#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <ctime>
#include <string>
#include <sstream>
#include <math.h>
#include <stack>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const int I = 2;
const int J = 3;
const int K = 4;

int table[5][5] = {	
{ 0, 0, 0, 0, 0},
{ 0, 1, I, J, K},
{ 0, I,-1, K,-J},
{ 0, J,-K,-1, I},
{ 0, K, J,-I,-1}
};

int mul(int a, int b) {
	int sign = 1;
	if (a < 0) {
		a *= -1;
		sign *= -1;
	}
	if (b < 0) {
		b *= -1;
		sign *= -1;
	}
	return sign * table[a][b];
}

int value(char c) {
	if (c == 'i') return I;
	if (c == 'j') return J;
	return K;
}

int inverse(int a) {
	if (a == 1 || a == -1) return a;
	return -a;
}

int divide(int a, int b) {
	return mul(a, inverse(b));
}




bool solve(const string& s) {

	int n = s.size();

	int left = 1;
	int left_id = 0;
	while (left_id < n && left != I) {
		left = mul(left, value(s[left_id]));
		++left_id;
	}

	int right = 1;
	int right_id = 1;
	right_id = n - 1;
	while (right_id >= left_id && right != K) {
		right = mul(value(s[right_id]), right);
		--right_id;
	}

	int mid = 1;
	for (int i = left_id; i <= right_id; ++i) {
		mid = mul(mid, value(s[i]));
	}

	return left == I && mid == J && right == K;
}

int main() {

	


	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
	#else
	#define taskname "cutting"
		//freopen(taskname".in","r",stdin);
		//freopen(taskname".out","w",stdout);
	#endif

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int l, x;
		string s;
		cin >> l >> x >> s;	

		string fs;
		for (int i = 0; i < x; ++i) {
			fs += s;
		}

		int answer = solve(fs);
		
		printf("Case #%d: %s\n", test, (answer ? "YES" : "NO"));
		eprintf("Case #%d: %s\n", test, (answer ? "YES" : "NO"));
	}



	return 0;
}