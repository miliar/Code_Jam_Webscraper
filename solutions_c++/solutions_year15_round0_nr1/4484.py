using namespace std;
#include <cstdio>
#include <iostream>

int main() {
	int tc;
	cin>>tc;
	for(int t = 1;t<=tc;t++) {
		int n, c = 0, sum = 0;
		cin>>n;
		string str;
		cin>>str;
		for(int i = 0;i<=n;i++) {
			sum += str[i] - '0';
			if(sum < i + 1) {
				c++;
				sum++;
			}
		}
		printf("Case #%d: %d\n", t, c);
	}
	return 0;
}