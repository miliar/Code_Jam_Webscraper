#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

string a;

int main()
{
	int T;
	scanf(" %d", &T);
	for(int t = 0; t < T; t ++) {
		int n;
		scanf(" %d", &n);
		cin >> a;
		int curr = 0;
		int newp = 0;
		for(int i = 0; i < a.length(); i ++) {
			
			if(curr >= i)
				curr += a[i] -'0';
			else if(a[i] > '0') {
				newp += i - curr;
				curr = i + a[i] - '0';
			}
		}
		printf("Case #%d: %d\n", t + 1, newp);
	}
	return 0;
}