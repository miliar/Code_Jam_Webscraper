#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> fs;

char bla[16];
int ispal(long long x) {
	sprintf(bla, "%lld", x);
	int sz = strlen(bla);
	for(int i = 0; i < sz/2; i++)
		if(bla[i] != bla[sz-i-1]) return 0;
	return 1;
}

int main()
{
	for(long long i = 1; i*i <= 100000000000000LL; i++)
		if(ispal(i) && ispal(i*i)) fs.push_back(i*i);
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ca++) {
		long long a, b;
		scanf("%lld%lld", &a, &b);
		printf("Case #%d: %d\n", ca, (int)(upper_bound(fs.begin(), fs.end(), b) - lower_bound(fs.begin(), fs.end(), a)));
	}
	return 0;
}
