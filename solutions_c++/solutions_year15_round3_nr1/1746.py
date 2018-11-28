#include <pe.h>

ll solve(ll R, ll C, ll W) {
	ll result = 0;
	if (R > 1) {
		result += (R-1)*C/W;
	}
	result += C/W +W-1;
	if (C%W!=0) {
		++result;
	}
	return result;
}

int main() {
	ll T, R, C, W;
	cin >> T;
	for (ll i = 0; i < T; ++i) {
		cin >> R; cin >> C; cin >> W;
		printf("Case #%Ld: %Ld\n", i+1, solve(R, C, W));
	}
	return 0;
}


