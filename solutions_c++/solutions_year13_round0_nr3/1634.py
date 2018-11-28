#pragma comment (linker, "/STACK:214721677")
#define _CRT_SECURE_NO_WARNINGS
#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <string>
using namespace std;
#define REP(i,n) for (int i=0, _n=(n)-1; i <= _n; ++i)
#define FOR(i,a,b) for (int i=(a), _b=(b); i <= _b; ++i)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int) ((a).size()))
const double Pi = acos(-1.0);
const double eps = 1e-10;
const double phi = 0.5 + sqrt(1.25);
const int INF = 1000*1000*1000 + 7;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;
typedef bool BOOL;
template < typename T > T sqr (T a) { return (a) * (a); }
template < typename T > T abs (T a) { return (a < 0) ? -(a) : (a); }
template < typename T > T gcd (T a, T b) { return (b) ? gcd(b, a % b) : a; }

#define YES 1
#define NO 0

BOOL isPalindrome(ll n)
{
	string lol = "";
	while (n)
	{
		lol += n % 10;
		n /= 10;
	}
	BOOL match = YES;
	for (int i = 0; i < lol.size() / 2; ++i)
		match &= (lol[i] == lol[lol.size() - 1 - i]);
	return match;
}

ll fairAndSquare[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002, 10000001};

int fine(ll N)
{
	int i = 0;
	int size = sizeof(fairAndSquare) / sizeof(ll);
	while (i < size && fairAndSquare[i] <= N)
	{
		++i;
	}
	return i;
}


int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	/*for (ll n = 1; n < 1e7 + 5; ++n)
	{
		if (isPalindrome(n) && isPalindrome(n * n))
			printf("%d, ", n);
	}
	cout << sizeof(fairAndSquare);
	return EXIT_SUCCESS;*/
	int Tests;
	scanf("%d\n", &Tests);
	for (int testNumber = 1; testNumber <= Tests; ++testNumber)
	{
		ll A, B;
		scanf("%lld%lld\n", &A, &B);
		printf("Case #%d: ", testNumber);
		printf("%d", fine(sqrt(1.0 * B)) - fine(sqrt(1.0 * A - 1)));
		printf("\n");
	}
	return EXIT_SUCCESS;
}
