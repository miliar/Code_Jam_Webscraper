#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))
#define pb(x) push_back(x)

typedef long long ll;

int t;
int n;
int m[1234];
int diff;
int first, second;

int main()
{
scanf("%d", &t);

for(int q=1; q<=t; q++) {
	scanf("%d", &n);
	for(int i=0; i<n; i++) scanf("%d", &m[i]);

	first=second=0;

	for(int i=0; i<n-1; i++) first+=max(m[i]-m[i+1], 0);

	diff=0;

	for(int i=0; i<n-1; i++) diff=max(diff, max(m[i]-m[i+1], 0));

	for(int i=0; i<n-1; i++) {
		second+=min(m[i], diff);
	}

	printf("Case #%d: %d %d\n", q, first, second);
}

	return 0;
}
