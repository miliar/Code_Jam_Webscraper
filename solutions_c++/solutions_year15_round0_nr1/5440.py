#include <pe.h>

using namespace std;

ll friends(ll smax, string shyness) {
	ll result = 0;
	ll partial_sum = 0;
	for (ll i = 0; i < smax+1; ++i) {
		if (shyness[i]-'0'!=0) {
			while (partial_sum < i) {
				++partial_sum;
				++result;
			}
			partial_sum+=shyness[i]-'0';
		}
	}
	return result;
}

int main() {
	ll T;
	cin >> T;
	ll smax;
	string shyness;

	for (ll i = 0; i < T; ++i) {
		cin >> smax;
		cin >> shyness;
		printf("Case #%Ld: %Ld\n", i+1, friends(smax, shyness));
	}

	return 0;
}

