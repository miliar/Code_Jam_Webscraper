#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
#include <map>
#include <deque>
#include <set>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(n);(i)++)
#define REP2(i,s,n) for(int(i)=s;(i)<(n);(i)++)
#define RREP(i,n) for(int(i)=n;(i)>=0;(i)--)

inline bool ck_pal(long long s)
{
	char c[20];
	int i = 0;
	while (s > 0) {
		c[i++] = s%10;
		s /= 10;
	}
	for (int j = 0; j < i/2; j++) {
		if (c[j] != c[i-j-1]) return false;
	}
	return true;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		long long a, b;
		cin >> a >> b;

		long long cnt = 0;
		for (long long k = 1; k*k <= b; k++) {
			if (k*k < a) continue;
			cnt += (ck_pal(k) && ck_pal(k*k));
		}
		
		printf("Case #%d: %d\n", t+1, cnt);
	}

	return 0;
}


