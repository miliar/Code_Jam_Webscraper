#include <iostream>
#include <cstdio>
using namespace std;
char s[1000];

int work(int l, int r, bool dir) {
	// cout<<l<<" "<<r<<" "<<dir<<endl;
	if(l > r) {
		return 0;
	}
	if(l == r && s[l] == '+') {
		if(dir)
			return 0;
		else 
			return 1;
	}
	if(l == r && s[l] == '-') {
		if(dir)
			return 1;
		else
			return 0;
	}
	if(dir) {
		for(int i = l; i <= r; i++) {
			if(s[i] == '-') {
				while(s[i] == '-' && i <= r) i++;
				return 1 + work(i, r, false);
			} else {
				while(s[i] == '+' && i <= r) i++;
				return 1 + work(i, r, true);
			}
		}
	} else {
		for(int i = r; i >= l; i--) {
			if(s[i] == '-') {
				while(s[i] == '-' && i >= l) i--;
				return 1 + work(l, i, false);
			} else {
				while(s[i] == '+' && i >= l) i--;
				return 1 + work(l, i, true);
			}
		}
	}
}

int main() {
	int t, cas = 0, len, count, i, j;
	scanf("%d", &t);
	while(t--) {
		scanf("%s", s);
		len = strlen(s);
		cas++;
		count = 0;
		j = len-1;
		while(s[j] == '+' && j >= 0) j--;
		count = work(0, j, true);

		printf("Case #%d: %d\n", cas, count);
	}
}