
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>

#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)

using namespace std;

typedef vector<int> vi;

int t;
int a, b;
int v[1001];

int solve() {
	int cont = 0;
	for (int i=a;i<=b;i++) {
		if(v[i])
			cont++;
	}
	return cont;
}

bool isPalindrome(int n) {
	stringstream stream;
	string number;
	stream << n;
	stream >> number;
	for (int i = 0;i<=number.size()/2;i++)
		if (number[i]!=number[number.size()-1-i])
			return false;
	return true;
}

bool isFairAndSquare(int n) {
	int root = (int)sqrt(n);
	return isPalindrome(n) && (root*root==n) && isPalindrome(root);
}

int main() {
	for (int i=1;i<=1000;i++) {
		if (isFairAndSquare(i)) {
			v[i] = 1;
		} else {
			v[i] = 0;
		}
	}

	scanf("%d", &t);
	for (int i=1; i<=t; i++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
