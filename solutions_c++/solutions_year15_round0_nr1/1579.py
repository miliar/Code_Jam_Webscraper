#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;


int main () {
	int T, n, x;
	string s;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		cin >> n >> s;
		int cur_sum = 0, rez = 0;
		for (int i = 0; i < s.length(); ++i) {
			if (cur_sum < i) {
				rez ++;
				cur_sum ++;
			}
			cur_sum += ((int)(s[i] - '0'));
		}


		printf("Case #%d: %d\n", t, rez);

	}
	return 0;
}
