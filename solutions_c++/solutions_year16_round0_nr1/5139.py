#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
int T;

bool ok(const vector<bool>& a){
	for (int i = 0; i < 10; i++){
		if (a[i] == false)
			return false;
	}
	return true;
}
void checker(vector<bool>& a,long long int n){
	while (n != 0){
		int now = n % 10;
		a[now] = true;
		n /= 10;
	}
}

string go(int n){
	if (n == 0)
		return "INSOMNIA";
	vector<bool> a(10);
	for (int i = 0; i < 10; i++)
		a[i] = false;
	long long ans;
	for (long long i = 1;; i++){
		ans = n*i;
		checker(a, ans);
		if (ok(a))
			break;
	}
	return to_string(ans);
}

int main() {
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");

	cin >> T;
	vector<int> a(T + 1);
	for (int t = 1; t <= T; t++){
		cin >> a[t];
	}
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		cout << go(a[t]) << "\n";
	}

	return 0;
}