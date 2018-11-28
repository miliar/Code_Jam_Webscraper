#include <pe.h>

ll maximum(vector<ll> pancakes) {
	ll result = 0;
	ll maxi = pancakes[0];
	for (ll i = 0; i < pancakes.size(); ++i) {
		if (pancakes[i] > maxi) {
			maxi = pancakes[i];
			result = i;
		}
	}
	return result;
}

ll minutes(vector<ll> pancakes) {
	ll index = maximum(pancakes);

	ll maxi = pancakes[index];
	if (maxi <= 3) {
		return maxi;
	}

	ll result = maxi;
	for (ll i = 2; i <= sqrt(maxi); ++i) {
		vector<ll> npancakes(pancakes);
		npancakes[index] = maxi/i; 
		npancakes.pb(maxi-maxi/i);
		result = min(result, 1+minutes(npancakes));
	}

	return result;
}

int main() {
	ll T;
	cin >> T;

	for (ll i = 0; i < T; ++i) {
		ll D;
		cin >> D;
		vector<ll> pancakes(D);
		for (ll j = 0; j < D; ++j) {
			cin >> pancakes[j];
		}
		printf("Case #%Ld: %Ld\n", i+1, minutes(pancakes));
	}

	return 0;
}
