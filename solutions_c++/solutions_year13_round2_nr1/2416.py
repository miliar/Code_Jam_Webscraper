#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
// Uncomment for libgmp
/*#include "gmpxx.h"
#define big mpz_class*/

using namespace std;

int a, n;

list<int> motes;
int maxi;

int ans;

bool can(list<int> motes) {
	int s = a;
	for (list<int>::iterator it = motes.begin(); it != motes.end(); it++) {
		if (*it >= s)
			return false;
		s += *it;
	}
	return true;
}

void backtracking(int i, int s, list<int> v) {
	if (can(v)) {
		if (i < ans)
			ans = i;
		return;
	}

	//printf("%d %d\n", v.front(), s);
	if (v.front() < s) {
		int a = v.front();
		v.pop_front();
		backtracking(i, s + a, v);
		return;
	}

	if (v.front() >= s && s > 1) {
		/*int a = s - 1;
		int s1 = s;
		int i1 = 0;
		while (v.front() >= s1) {
			s1 += a;
			a = s1 - 1;
			i1++;
		}*/
		backtracking(i + 1, s + s - 1, v);
	}

	v.pop_back();
	backtracking(i + 1, s, v);
}
 
int main()
{
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
    	fprintf(stderr, "Case #%d of %d...\n", c, t);
    	scanf("%d %d", &a, &n);
    	maxi = 0;
    	ans = 1e9;
    	motes.clear();
    	//motes.assign(n, int());
    	for (int i = 0; i < n; i++) {
    		int b;
    		scanf("%d", &b);
    		motes.push_back(b);
    		if (b > maxi) maxi = b;
    	}

    	motes.sort();

    	backtracking(0, a, motes);

    	printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}
