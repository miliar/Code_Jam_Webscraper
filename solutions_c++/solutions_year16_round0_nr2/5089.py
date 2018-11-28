#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<set>
#include<unordered_set>
#include<algorithm>
using namespace std;

string s;

void work() {
	int ans = 0;
	char ch = '+';
	for (int i=s.size()-1; i>=0; i--) {
		if (s[i] != ch) {
			ans++;
			if (ch == '+') ch = '-';
			else ch = '+';
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int t;
	scanf("%d\n", &t);
	for(int i=0;i<t;i++) {		
		getline(cin, s);
		printf("Case #%d: ", i+1);
		work();
	}

	return 0;
}

