#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
int T;

int go(string cake){
	int ans = 0;

	for (int i = 0; i < cake.length(); i++){
		bool blank = false;
		while (i < cake.length() && cake[i] == '-'){
			i++;
			blank = true;
		}
		if (blank)
			ans++;
		if (i + 1 < cake.length() && cake[i + 1] == '-'){
			ans++;
		}
	}


	return ans;
}

int main() {
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");

	cin >> T;
	vector<string> a(T + 1);
	for (int t = 1; t <= T; t++){
		cin >> a[t];
	}
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		cout << go(a[t]) << "\n";
	}

	return 0;
}