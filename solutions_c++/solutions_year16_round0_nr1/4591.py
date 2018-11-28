#include <string>
#include <iostream>
#include <set>

typedef long long ll;

ll solve(ll n)
{
	if (n == 0) return -1;

	std::set<char> s;
	ll nn = n;
	ll m = 1;

	while (s.size() != 10) {
		nn = n * m;
		std::string str = std::to_string(nn);
		for(auto it=str.begin(); it!=str.end(); ++it) {
			s.insert(*it);
		}
		++m;
	}

	return nn;
}

int main()
{
	int T;
	std::cin >> T;

	for (int t=1; t<=T; ++t) {
		ll N;
		std::cin >> N;
		ll ans = solve(N);
		if (ans == -1) {
			std::cout << "Case #" << t << ": INSOMNIA" << std::endl;
		} else {
			std::cout << "Case #" << t << ": " << ans << std::endl;
		}
	}

	return 0;
}