#include<iostream>
#include<fstream>

using namespace std;

#define LL long long

LL check(LL n){
	int a[10] = {0};
	int cnt = 0;
	LL k = 1;
	while(cnt < 10){
		LL m = k * n;
		while(m){
			if(!a[m % 10ll]){
				a[m % 10ll] = 1;
				cnt++;
			}
			m /= 10ll;
		}
		k++;
	}
	return (k - 1ll) * n;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int n;
		cin >> n;
		cout << "Case #" << i + 1 << ": ";
		if(n == 0)
			cout << "INSOMNIA" << endl;
		else
			cout << check(n) << endl;
	}

	return 0;
}