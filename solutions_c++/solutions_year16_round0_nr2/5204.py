#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++){
		cout << "Case #" << (test + 1)<< ": ";
		char a[200] = { 0 };
		cin >> a;
		int n = strlen(a);
		int result = 0;
		for (;;){
			int i;
			for (i = 0; i < n && a[i] == '+'; i++);
			if (i == n) break;
			if (i > 0) result++;
			for (; i < n && a[i] == '-'; i++);
			for (int j = 0; j < i; j++) a[j] = '+';
			result++;
		}
		cout << result << endl;
	}
}