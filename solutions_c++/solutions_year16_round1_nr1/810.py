#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;
int n;
char s[1234];
char ans[1234];

int main()
{
	scanf("%d\n", &t);
	for(int q=1; q<=t; q++) {
		scanf("%s\n", s);
		n=strlen(s);
		int p=0, r=n-1;
		for(int i=n-1; i>=0; i--) {
			int l=1;
			for(int j=0; l && j<i; j++) {
				if(s[j]>s[i]) l=0;
			}
			if(l) {
				ans[p++]=s[i];
			} else {
				ans[r--]=s[i];
			}
		}
		ans[n]=0;
		printf("Case #%d: %s\n", q, ans);
	}

	return 0;
}
