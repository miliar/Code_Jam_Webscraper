#include <bits/stdc++.h>

#define INF 1000000000
#define MOD 1000000007
#define MAXN 1000005
#define ins insert
#define pb push_back
#define mp make_pair
#define sz size
#define sd(n) scanf("%d",&n)
#define sll(n) scanf("%I64d",&n)
#define pdn(n) printf("%d\n",n)
#define plln(n) printf("%I64d\n",n)
#define pd(n) printf("%d ",n)
#define nl() printf("\n")
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int, int> pii;	

int main() {
	int t; sd(t);
	for(int i = 0; i < t; ++i) {
		int n; sd(n);
		char s[n+1]; scanf("%s", s);
		int ans = 0, curr = s[0]-'0';
		for(int j = 1; j < n+1; ++j) {
			if(curr < j) {
				int temp = j-curr;
				curr += temp;
				ans += temp;
			}
			curr += s[j]-'0';
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}	