#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<climits>
#include<cmath>
#include<cstring>
using namespace std;
typedef long long ll;

#define y1 mine
#define mp make_pair

double pi = acos(-1);

bool check[20];

ll check_digits(ll val){
	ll cnt = 1;
	
	for (; cnt <= 500000; cnt++){
		ll name = val*cnt;
		while (name != 0){
			check[name % 10] = true;
			name /= 10;
			int i;
			for (i = 0; i < 10; i++){
				if (!check[i]) break;
			}
			if (i == 10){
				return val*cnt;
			}
		}
	}

	return -1;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin >> T;
	for (int i = 0; i < T; i++){
		
		memset(check, false, sizeof(check));
		ll val; cin >> val;

		ll res = check_digits(val);
		
		if(res > 0) printf("Case #%d: %lld\n", i + 1, res);
		else printf("Case #%d: INSOMNIA\n", i + 1);

	}
	
	return 0;
}


