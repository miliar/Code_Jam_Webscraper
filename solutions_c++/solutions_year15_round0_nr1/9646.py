#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	// your code goes here
	int t, smax;
	scanf("%d", &t);
	for (int a = 1; a < t+1; a++) {
		scanf("%d", &smax);
		string s;
		cin >> s;
		int count = 0;
		int currSO = 0;
		int k;
		
		k = s[0] - '0';
		currSO += k;
		
		for (int i = 1; i < s.size(); i++) {
			k = (s[i] - '0');
			if (k != 0) {
				if (currSO < i) {
					count += (i - currSO);
					currSO += (i - currSO);
				}
			}
			currSO += k;
		}
		printf("Case #%d: %d\n", a, count);
	}
	return 0;
}