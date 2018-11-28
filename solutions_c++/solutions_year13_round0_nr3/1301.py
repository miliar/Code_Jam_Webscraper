#include <cstdio>
#include <cstring>

typedef long long ll;

int cnt(ll x) {
	ll t[] = {1LL, 4LL, 9LL, 121LL, 484LL, 10201LL, 12321LL, 14641LL, 40804LL, 44944LL, 1002001LL, 1234321LL, 4008004LL, 100020001LL, 102030201LL, 104060401LL, 121242121LL, 123454321LL, 125686521LL, 400080004LL, 404090404LL, 10000200001LL, 10221412201LL, 12102420121LL, 12345654321LL, 40000800004LL, 1000002000001LL, 1002003002001LL, 1004006004001LL, 1020304030201LL, 1022325232201LL, 1024348434201LL, 1210024200121LL, 1212225222121LL, 1214428244121LL, 1232346432321LL, 1234567654321LL, 4000008000004LL, 4004009004004};
	int i;
	for(i=0;i<39;i++){
		if(x<t[i])break;
	}
	return i;
}

//bool palindromes(char *s) {
//	int l = 0, r = strlen(s) - 1;
//	while(l < r) {
//		if(s[l] != s[r])
//			return false;
//		l++;
//		r--;
//	}
//	return true;
//}

int main() {
//	char a[100];
//	for(long long i = 1; i <= 10000000; i++) {
//		sprintf(a, "%lld", i);
//		if(palindromes(a)) {
//			long long ii = i * i;
//			sprintf(a, "%lld", ii);
//			if(palindromes(a)) {
//				puts(a);
//			}
//		}
//	}
	int t,c;
	ll a,b;
	scanf("%d",&t);
	for(c=1;c<=t;c++){
		scanf("%lld%lld",&a,&b);
		int ans = cnt(b) - cnt(a - 1);
		printf("Case #%d: %d\n",c,ans);
	}
	return 0;
}
