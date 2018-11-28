#include <iostream>
#include <string>
using namespace std;

int main () { 
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		int n;
		cin >> n;
		string s;
		cin >> s;
		int toInvite = 0;
		int sum = s[0] - '0';
		for (int i = 1; i < s.size(); i++) {
			if (sum < i) {
				toInvite += i - sum;
				sum += i - sum;
			}
			sum += s[i] - '0';
		}
		printf("%d\n", toInvite);
	}
	return 0;
}
