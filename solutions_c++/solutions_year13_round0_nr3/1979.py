#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long ll;

vector <ll> d;

bool check(ll x){
	char s[26];
	sprintf(s, "%lld", x);
	int l = strlen(s);
	for (int i = 0; i < l / 2; i++)
		if (s[i] != s[l - i - 1])
			return false;
	return true;
}

void precalc(){
	for (ll i = 1; i <= 11000000; i++)
		if (check(i) && check(i * i))
			d.push_back(i * i);
	d.push_back(1000000000000000000ll);
}

int main(){
	precalc();
	int t;
	ll a, b;
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++){
		scanf("%lld%lld", &a, &b);
		printf("Case #%d: %d\n", i + 1, upper_bound(d.begin(), d.end(), b) - lower_bound(d.begin(), d.end(), a));
		
	}
}
