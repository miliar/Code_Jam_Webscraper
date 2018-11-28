#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, sum, ans, tc = 0;
	string s;
	cin >> t;
	while (t--) {
		cin >> n >> s;
		sum = ans = 0;
		for (int i = 0; i <= n; ++i)
			s[i] -= '0';
		for (int i = 0; i <= n; ++i) {
			if (s[i]) {
				if(sum < i){
					ans += i - sum;
					sum = i;
				}
			}
			sum += s[i];
		}
		printf("Case #%d: %d\n", ++tc, ans);
	}
	return 0;
}