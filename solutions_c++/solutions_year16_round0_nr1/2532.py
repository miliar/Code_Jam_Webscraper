#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>

using namespace std;

bool track[10];

bool all() {
	bool result = true;
	for (int i = 0; i < 10; i++) {
		result &= track[i];
	}
	return result;
}

void update(int n) {
	while (n > 0) {
		track[n%10] = true;
		n /= 10;
	}
}

void eval(int n) {
	for (int i = 0; i < 10; i++) {
		track[i] = false;
	}
	
	int cur_number = n;
	int counter = 0;
	while (!all() && counter < 500) {
		update(cur_number);
		cur_number += n;
		counter++;
	}
	
	if (counter >= 100) {
		cout << "INSOMNIA";
		return;
	}
	cout << cur_number - n;
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << "Case #" << i + 1 << ": ";
		eval(n);
		cout << endl;
	}
		
	return 0;
}

