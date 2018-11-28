#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<cstring>
#include<cctype>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include<string>
#include<ctime>
#include<numeric>
#include<functional>
using namespace std;

#define eps 1e-8
#define PI 3.1415926
#define LL long long
#define ULL unsigned long long
#define MP make_pair
#define wait system( "pause" );

#define maxs 1024

int smax;
char s[maxs];

int cur, ans;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ca = 1; ca <= t; ++ca) {
		scanf("%d%s", &smax, s);
		cur = ans = 0;
		for (int shy = 0; shy <= smax; ++shy) {
			if (cur < shy) {
				ans += shy - cur;
				cur = shy;
			}
			cur += s[shy] - '0';
		}
		printf("Case #%d: %d\n", ca, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
