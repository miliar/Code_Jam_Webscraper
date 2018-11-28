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

ll n;
int job;
ll val[20];
ll quo[20];

ll power(ll a, ll b){
	ll res = 1;
	while (b > 0){
		if (b % 2 == 1) {
			res *= a;
			b--;
		}
		a *= a;
		b /= 2;
	}
	return res;
}

void make_val(ll a, ll i){
	ll b = 0;
	ll res = 0;
	while (i > 0){
		if (i % 2 == 1){
			res += power(a, b);
		}
		i >>= 1;
		b++;
	}
	val[a] = res;

}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int t = T;

	cout << "Case #1:" << endl;
	while (T--){
		int cnt = 0;
		cin >> n >> job;

		ll limit = 1;

		limit <<= (n);


		for (ll i = (1 << n-1) + 1; i < limit && cnt != job; i+=2){
			bool flag = true;
			for (ll j = 2; j <= 10; j++){
				make_val(j, i);
				ll k;
				for (k = 2; k <= sqrt(val[j]); k++){
					if (val[j] % k == 0){
						quo[j] = k;
						break;
					}
				}
				if (k > sqrt(val[j]))
					flag = false;

			}

			if (flag) {
				cnt++;
				cout << val[10];
				for (int idx = 2; idx <= 10; idx++){
					cout << " " << quo[idx];
				}
				cout << endl;
				/*
				cout << i << ": ";
				for (int idx = 2; idx <= 10; idx++){
					cout << quo[idx] << " ";
				}
				cout << endl;
				
				cout << i << ": ";
				for (int idx = 2; idx <= 10; idx++){
					cout << val[idx] << " ";
				}
				cout << endl << endl;
				*/
			}
		}




	}

	
	return 0;
}


