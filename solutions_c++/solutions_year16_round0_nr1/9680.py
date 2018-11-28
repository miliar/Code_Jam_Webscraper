#include <iostream>
#include <vector>

#define MAX_T   (100)
#define MAX_N   (1000000LL)

using namespace std;

inline void count(vector<bool> &a, long long ni) {
	int digit;

	while(ni) {
		digit = ni % 10;
		a[digit] = true;
		ni /= 10;
	}
}

inline bool check(const vector<bool> &a) {
	for(bool b : a)
		if(!b)
			return false;
	return true;
}

long long countSheep(int n) {
	if(n == 0)
		return -1;

	vector<bool> appear(10, false);
	for(long long i = 1; i <= MAX_N; ++i) {
		long long ni = n * i;
		count(appear, ni);
		if(check(appear))
			return ni;
	}

	return -1;
}

int main(void) {
	cout.sync_with_stdio(false);

	int nTests;
	cin >> nTests;

	for(int t = 1; t <= nTests; ++t) {
		int n;
		cin >> n;
		cout << "Case #" << t << ": ";

		long long ans = countSheep(n);
		if(ans < 0LL)
			cout << "INSOMNIA" << endl;
		else
			cout << ans << endl;
	}

	return 0;
}
