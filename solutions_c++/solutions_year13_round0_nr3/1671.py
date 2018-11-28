#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <algorithm>
#include <bitset>
#include <set>

using namespace std;

#define REP(i,n) for(long long int i = 0; i < int(n); ++i)
#define REPV(i, n) for (long long int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(long long int i = (int)(a); i < (int)(b); ++i)

#define ALL(v) (v).begin(), (v).end()
#define PF push_front
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define lli long long int

bool pal(lli a) {
	string s = std::to_string(a);
	int len = s.length();
	for (int i = 0; i < len/2; i++) {
		if (s[i] != s[len - i - 1]) {
			return false;
		}
	}
	return true;
}

const int N = 10000000 + 2;
int sum[N];

int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int psum = 0;
	for(lli i = 1; i < N; ++i) {
		if (pal(i) && pal(i*i)) psum++;
		sum[i] = psum;
	}
	int T;
	cin >> T;
	lli A, B;
	REP(i, T) {
		cin >> A >> B;
		int a = ceil(sqrt(-0.5 + A)), b = (int)sqrt(0.5 + B);
		cout << "Case #" << (i + 1) << ": " << (sum[b] - sum[a-1]) << endl; 
	}
    return 0;
}