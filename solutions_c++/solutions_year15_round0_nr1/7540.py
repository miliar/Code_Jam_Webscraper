#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;
#define sz 1009

char S[sz];
int n, ans, pre;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		scanf("%d %s", &n, S);
		ans = pre = 0;
		for(int ii=0;ii<=n;ii++) {
			if(pre+ans < ii) {
				ans += ii-(pre+ans);
			}
			pre += S[ii]-'0';
		}
		printf("Case #%d: %d\n", i, ans);
	}
}
