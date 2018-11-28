#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define MAX 100000000000000ll

vector <int> fairSquares;

bool isPalindrome(long long N) {
    vector <int> v;

    while (N != 0) {
        v.push_back(N % 10);
        N /= 10;
    }

    for (int i=0; i < v.size() / 2; ++i) {
        if (v[i] != v[v.size() - i - 1]) {
            return false;
        }
    }

    return true;
}

void generate() {
    long long ans = 0;
    for (long long k = 1; k * k <= MAX; ++k) {
        if (isPalindrome(k) && isPalindrome(k * k)) {
            fairSquares.push_back(k * k);
        }
    }
}

int main() {
	int T = 1;
    int t;

    generate();

    scanf("%d", &t);
    while (t--) {
        long long A, B;
        scanf("%lld %lld\n", &A, &B);

        int ans = 0;
        for (int i=0; i < fairSquares.size(); ++i) {
            if (A <= fairSquares[i] && fairSquares[i] <= B) {
                ++ans;
            }
        }

        printf("Case #%d: %d\n", T++, ans);
    }
	
	return 0;
}
