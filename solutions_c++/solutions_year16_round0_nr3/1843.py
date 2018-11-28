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

int main() {
	int t;
	scanf("%d", &t);
	puts("Case #1:\n");

	int n, m;
	scanf("%d%d", &n, &m);
	for(int i=0, j=0; i<(1<<((n/2)-1)) && j<m; i++, j++) {
		printf("1");
		for(int k=0; k<(n-2)/2; k++) {
			if((i>>k) & 1)	printf("11");
			else	printf("00");
		}
		printf("1 ");
		for(int k=3; k<=11; k++)	printf("%d%c", k, " \n"[k==11]);
	}

    
    return 0;
}
