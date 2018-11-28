#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int solve() {
	int R, C, W;
	cin >> R >> C >> W;
	int ret;

	int diff = C-W;
	// printf(" %d %d %d\n", R, C, W);
	int a = 0;
	if ((C%W) != 0)
		a = 1;
	if(diff == 0)
		return R * C;
	else
		return R * ((C / W) -1 + W + a);

	return ret;
}

int main() {
	int t;
	cin >> t;

	for(int i = 0; i < t; i++)
		printf("Case #%d: %d\n", i+1, solve());

	return 0;
}
