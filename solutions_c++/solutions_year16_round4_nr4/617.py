#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

#define double long double


int n;
int a[10];


bool check2(int i,int m,int mask) {
	if(i==n) return true;
	int p = n*a[i];
	int count = 0;
	bool ans = true;
	for(int j=0;j<n;++j) {
		int c = 1<<(p+j);
		// vie ovladat && free
		if((mask&c) && (m&(1<<j))) {
			// sadne si za masinu
			++count;
			// da sa to dokoncit
			ans = ans && check2(i+1,m^(1<<j),mask);
		}
	}
	// sadol si za masinu cize sa neflaka
	if(count) return ans;
	// nesadol si cize sa flaka
	else return false;
}
	



bool check(int mask) {
	FOR(i,10) a[i]=i;
	bool ans = true;
	do {
		bool temp = check2(0,(1<<n)-1,mask);
		ans = ans && temp;
	} while(next_permutation(a,a+n));
	return ans;
}
	
int main(void) {
	int t;
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;++tt) {
		printf("Case #%d: ",tt);
		scanf("%d\n",&n);
		int mask = 0;
		FOR(i,n) {
			char s[10];
			scanf("%s\n",s);
			FOR(j,n) {
				mask<<=1;
				mask|=s[j]-'0';
			}
		}
		
		int cc = n*n;
		int ans = cc;
		FOR(i,1<<cc) {
			int total = __builtin_popcount(i);
			if(check(mask|i)) ans = min(ans,total);
		}
		printf("%d\n",ans);
		
	}
}