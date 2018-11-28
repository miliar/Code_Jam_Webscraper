#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
typedef long long ll;

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++){
		cout << "Case #" << (test + 1)<< ": ";
		int n;
		cin >> n;
		bool has[10] = { 0 };
		int cnt = 0, x = 0;
		for (int i = 1; i <= 100 && cnt < 10; i++){
			x = i * n;
			while (x){
				cnt = cnt - has[x % 10] + 1;
				has[x % 10] = 1;
				x /= 10;
			}
			x = i * n;
		}
		if (cnt < 10){
			cout << "INSOMNIA";
		}
		else{
			cout << x;
		}
		cout << endl;
	}
}