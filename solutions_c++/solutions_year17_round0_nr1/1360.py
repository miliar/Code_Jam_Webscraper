#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int N_MAX = 1010;

void flip(char &c) {
	if(c=='+')
		c='-';
	else
		c='+';
}

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		char s[N_MAX];
		int k;
		scanf("%s%d", s, &k);
		int n=strlen(s);
		int ans=0;
		for(int i=0; i<=n-k; i++) {
			if(s[i] != '+') {
				ans++;
				for(int j=i; j<i+k; j++)
					flip(s[j]);
			}
		}
		bool ok=true;
		for(int i=n-k+1; i<n && ok; i++) {
			if(s[i] != '+')
				ok=false;
		}
		if(ok)
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
