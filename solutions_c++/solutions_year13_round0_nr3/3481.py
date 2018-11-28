#include <cstdio>
#include <algorithm>

#define MAX 10000020
typedef long long ll;

int cc;

int list[MAX], lFull;

bool isPalindrome(ll t){
	char split[20];
	int sFull=0;

	while(t){
		split[sFull++] = t%10;
		t /= 10;
	}

	int i;
	for(i=0; i<sFull/2; i++)
		if(split[i] != split[sFull-1-i])
			return false;

	return true;
}

void init(){
	ll i;
	for(i=1; i<=MAX; i++){
		if(isPalindrome(i) && isPalindrome(i*i))
			list[lFull++] = i*i;
	}
}

void solve(){
	ll a, b;
	scanf("%lld%lld", &a, &b);
	printf("%d\n", (std::upper_bound(list, list+lFull, b)-list)-(std::lower_bound(list, list+lFull, a)-list));
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	init();
	
	for(cc=1; cc<=t; cc++){
		printf("Case #%d: ", cc);

		solve();
	}

	return 0;
}