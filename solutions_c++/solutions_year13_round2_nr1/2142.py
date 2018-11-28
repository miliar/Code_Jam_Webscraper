#include <cstdio>
#include <algorithm>
using namespace std;

int ar[100], o, result;
void solve(int ci, long long mote, int curr) {
	if(curr < o) {
		if(ci == o) {
			if(result > curr)
				result = curr;
			return;
		}
		if(mote > ar[ci]) solve(ci+1, mote+ar[ci], curr);
		else {
			solve(ci, mote + mote - 1, curr+1);
			solve(ci+1, mote, curr+1);
		}
	}
}
int main() {
	int tc;
	scanf("%d", &tc);
	for(int cs=1; cs<=tc; cs++) {
		printf("Case #%d: ", cs);
		int mote;
		scanf("%d %d", &mote, &o);
		for(int i=0; i<o; i++)
			scanf("%d", ar+i);
		sort(ar, ar+o);
		result = o;
		solve(0, mote, 0);
		printf("%d\n", result);
	}
	return 0;
}
