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

const int MAXN = 100 + 10;

char s[MAXN];

int main() {
	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		scanf("%s", s);
		int n = strlen(s), cnt = 0;
		char prv = s[0];
		for(int i=0; i<n; i++) {
			if(s[i] != prv) {
				cnt++;
				prv = s[i];
			}
		}
		printf("Case #%d: %d\n", kase, cnt + (s[n-1]=='-'));
	}
    
    return 0;
}
