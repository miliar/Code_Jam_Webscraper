#include <bits/stdc++.h>

using namespace std;

int x, r, c;

string compute() {
	if((r * c) % x != 0)
		return "RICHARD";
	
	if(min(r, c) < x - 1)
		return "RICHARD";

	
	return "GABRIEL";
}

int main() {
	int t;
	cin >> t;
	
	for(int i = 0; i < t; ++i) {
		cin >> x >> r >> c;
	
		cout << "Case #" << i + 1<< ": " << compute() << '\n';
	}
}