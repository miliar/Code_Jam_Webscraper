#include <iostream>
#include <set>
#define ll long long
using namespace std;
int arr[10];
ll solve(ll n){
	for(int i = 0; i < 10; i++){
		arr[i] = 0;
	}
	int cnt = 0;
	ll temp, val = 0, ret = 0;
	while(cnt < 10){
		val += n;
		temp = val;
		while(temp){
			int x = temp % 10;
			if(arr[x] == 0){
				arr[x] = 1;
				cnt++;
			}
			temp /= 10;
		}
	}
	return val;
}

int main() {
	int t, n;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cout << "Case #"<< i <<": ";
		cin >> n;
		if(n == 0){
			cout << "INSOMNIA";
		}
		else{
			cout << solve(n);
		}
		cout << endl;
	}
	return 0;
}