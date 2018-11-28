#include <iostream>
#include <cstdio>
using namespace std;

int smax, shy[1010];
char shy_s[1010];

int main()
{
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		cin >> smax >> shy_s;
		for (int i = 0; i < smax+1; i++)
			shy[i] = shy_s[i] - '0';
		int total = 0, ans = 0;
		for (int i = 0; i < smax+1; i++) {
			if (total < i && shy[i]) {
				ans += (i - total);
				total += (i - total);
			}
			total += shy[i];
		}
		cout << "Case #" << kase << ": " << ans << endl;
	}
	return 0;
}

