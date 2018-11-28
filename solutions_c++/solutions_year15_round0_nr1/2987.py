#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main()
{
	int T; cin >> T;
	for (int t = 1; t<=T; t++) {
		int maxShy; cin >> maxShy;
		string shyLevel; cin >> shyLevel;
		int counter = shyLevel[0] - '0';
		int ans = 0;
		for (int i = 1; i <= maxShy; i++) {
			int n = shyLevel[i] - '0';
			if (n > 0) {
				if (counter < i) {
					ans += i-counter;
					n += i-counter;
				}
			}
			counter += n;
		}
		std::cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}