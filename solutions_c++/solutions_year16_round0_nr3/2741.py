#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cassert>

#define SHOW(...) {;}
#define REACH_HERE {;}
#define PRINT(s, ...) {;}
#define PRINTLN(s, ...) {;}

// #undef HHHDEBUG
#ifdef HHHDEBUG
#include "template.h"
#endif

using namespace std;

template<typename T>
using Grid = vector<vector<T>>;

const double E = 1e-8;
const double PI = acos(-1);

#define SMALL true
#if (SMALL)
const int n = 16;
const int j = 50;
#else
const int n = 32;
const int j = 500;
#endif


// const int n = 4;
// const int j = 3;

// const int UP_LIMIT = 1 << (n + 1);
// int is_prime[UP_LIMIT + 1];
// void fill_prime() {
// 	for (int i = 1; i <= UP_LIMIT; i++) // init to 1
// 	    is_prime[i] = 1;
// 	for (int i = 4; i <= UP_LIMIT; i += 2) // even number is not
// 	    is_prime[i] = 0;
// 	for (int k = 3; k*k <= UP_LIMIT; k++) // start from 9, end at sqrt
// 	    if (is_prime[k])
// 	        for(int i = k*k; i <= UP_LIMIT; i += 2*k) // every two is not 
// 	            is_prime[i] = 0;
// }

vector<vector<long long>> ans;

long long interprete(long long x, int base) {
	long long ret = 0;
	long long y = 1;
	while (x) {
		if (x & 1)
			ret += y;
		y *= base;
		x >>= 1;
	}
	return ret;
}

long long div(long long x) {
    if (x % 2 == 0)
        return 2;
    long long t = sqrt(x);
    for (long long i = 3; i <= t; i += 2)
        if (x % i == 0)
            return i;
    return -1;
}

void test(long long x) {
	if (ans.size() == j)
		return ;
	if ((x & 1) == 0)
		return ;

	vector<long long> a;
	a.push_back(interprete(x, 10));
	for (int base = 2; base <= 10; base++) {
		long long val = interprete(x, base);
		long long d = div(val);
		// SHOW(val, d)
		if (d != -1)
			a.push_back(d);
		else
			break;
	}
	if (a.size() == 10)
		ans.push_back(a);
}

int main() {
    ios::sync_with_stdio(false);

    long long x = (1 << (n-1)) + 1;
    long long y = 1 << n;
    for (long long i = x; i < y; i++) {
    	test(i);
    }

    // 110111
    // test((1<<6) - 1 - (1<<3));
    printf("Case #1:\n");
    for (const auto& a : ans) {
    	for (long long x : a) {
    		printf("%lld ", x);
    	}
    	printf("\n");
    }
}







