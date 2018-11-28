#include <cstdio>

int solve(int n) {
	
	bool h[10];
	for (int i=0;i<10;i++) h[i] = false;
	for (int i=1;i<100000;i++) {
		
		long long t = n*i;
		while(t>0) {
			
			h[t%10] = true;
			t/=10;
		}
		bool ans = true;
		for (int j=0;j<10;j++) 
			ans&=h[j];
		if (ans)
			return n*i;
	}
	return -1;
}

int main() {
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t, ans, n;
	scanf("%d", &t);
	for (int i=0;i<t;i++) {
		
		scanf("%d", &n);
		ans = solve(n);
		if (ans!=-1)
			printf("Case #%d: %d\n", i+1, ans);
		else
			printf("Case #%d: INSOMNIA\n", i+1);
	} 
	return 0;
}
