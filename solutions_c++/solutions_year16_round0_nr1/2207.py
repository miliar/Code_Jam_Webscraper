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

bool used[10];

bool check() {
	for(int i=0; i<10; i++)	if(!used[i])	return false;
	return true;
}

int solve(int x, int n) {
	int tmp = x;
	while(x) {
		used[x%10] = true;
		x /= 10;
	}
	if(check())	return tmp;
	return solve(tmp+n, n);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		int x;
		scanf("%d", &x);
		fill(used, used+10, false);
		
		printf("Case #%d: ", kase);
		if(!x)	puts("INSOMNIA");
		else	printf("%d\n", solve(x, x));
	}
    
    return 0;
}
