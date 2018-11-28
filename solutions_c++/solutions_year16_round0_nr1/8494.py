#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

void problem()
{
	int n;
	cin >> n;
	
	if(n == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}
	
	bool b[10] = {};
	
	for(int i = 0; ; ++i) {
		int ni = n * i;
		
		while(ni > 0) {
			b[ni % 10] = true;
			ni /= 10;
		}
		
		bool f = true;
		for(int j = 0; j < 10; ++j) {
			if(b[j] == false) f = false; 
		}
		if(f) {
			cout << i * n << endl;
			return;
		}
	}
}

int main() {
	
	int t;
	cin >> t;
	
	for(int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		problem();
	}
	
	return 0;
}