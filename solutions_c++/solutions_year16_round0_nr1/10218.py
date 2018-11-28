#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

void mapDigits(long long int val, bool a[]) {
	
	while(val > 0) {
		a[val%10] = true;
		val /= 10;
	}	
}

bool digitsMapped(bool a[]) {
	bool res = true;
	for(int i = 0; i < 10; i++) {
		res = res && a[i];
	}
	return res;
}

int main() {
	long long int n, ans;
	
	int t;
	cin >> t;
	bool a[10];
	for(int i = 0; i < t; i++) {
		ans = 0;
		string res = "Case #" + to_string(i+1) + ": ";
		cin >> n;
		for(int j = 0; j < 10;j ++) {
			a[j] = false;
		}
		
		if(n == 0) {
			cout << res + "INSOMNIA" + "\n";
		}
		else {
			for(int k = 1; k >= 0; k++) {
				long long int val = n * k;
				mapDigits(val, a);
				if(digitsMapped(a)) {
					ans = val;
					break;
				}
			}	
			cout << res + to_string(ans) + "\n";
		}
	}
	return 0;
}
