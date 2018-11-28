#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define ll long long
#define EPS 1e-7
using namespace std;
bool check(int a[]){
	for (int i = 0; i < 10; ++i){
		if (a[i] == 0)
			return false;
	}
	return true;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ll t, n,ans=0;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n;
		ans = 1;
		int cnt = 1;
		int a[10] = { 0 };
		if (n == 0){
			cout << "Case #" << k << ": INSOMNIA\n";

		}
		else{
			while (!check(a)){
				ans = n*cnt++;
				ll tmp = ans;
				while (tmp != 0){
					a[tmp % 10] = 1;
					tmp /= 10;
				}
			}
			cout << "Case #" << k << ": " << ans << endl;
		}
	}


	
	
	//system("pause");
}