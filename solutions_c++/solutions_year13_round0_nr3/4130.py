#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

const long long MAX = 1e14;
char s[25];
vector<long long> fs;

bool palin(long long x) {
	sprintf(s, "%lld", x);
	for(int i = 0, j = strlen(s) - 1; i < j; ++i, --j)
		if(s[i] != s[j]) return false;
	return true;
}

void init() {
	for(long long i = 1; i * i <= MAX; ++i)
		if(palin(i) && palin(i*i)) fs.push_back(i*i);
}

int main() {
	init();
	int tc; scanf("%d", &tc);
	for(int i = 1; i <= tc; ++i) { 
		long long a, b; scanf("%lld%lld", &a, &b);
		printf("Case #%d: %d\n", i, upper_bound(fs.begin(), fs.end(), b) - lower_bound(fs.begin(), fs.end(), a));
	}
	return 0;
}
