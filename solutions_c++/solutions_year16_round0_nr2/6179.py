#include <bits/stdc++.h>
#define pb push_back
#define popb pop_back
#define mkp make_pair
#define par pair<ll, ll>
#define N 200010

typedef long long ll;

using namespace std;

int main(){

	ll n, m, i, k, j;

	scanf("%lld\n", &n);

	string s;
	for(i = 1; i <= n; i++){
		getline(cin, s);

		printf("Case #%lld: ", i);

		k = 0;
		char c = s[0];

		for(j = 1; j < s.length(); j++){
			if(s[j] == c)
				continue;
			else{
				k++;
				c = s[j];
			}
		}

		if(c == '-')
			k++;

		printf("%lld\n", k);
	}

	return 0;
}
