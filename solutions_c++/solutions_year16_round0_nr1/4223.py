#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back

#define MOD 1000000007LL

ll solve(int n){
	if (n == 0) return -1;
	set<int> st;
	ll h = n;
	while (st.size() < 10){
		ll t = h;
		while (t){
			st.insert(t % 10);
			t /= 10;
		} 
		if (st.size() == 10) return h;
		h = h + (ll)n;
	}
	return -1;
}
int main(){
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		int a;
		scanf("%d", &a);
		ll res = solve(a);
		if (res == -1)
			printf("Case #%d: INSOMNIA\n", i);
		else 
			printf("Case #%d: %lld\n", i, res);
	}
	return 0;
}