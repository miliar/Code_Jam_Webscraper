#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>

using namespace std;

void eval() {
	string s;
	cin >> s;
	int result = 0;
	for (int i = (int)s.size() - 2; i >= 0; i--) {
		if (s[i] != s[i + 1]) result++; 
	}
	if (s[(int)s.size() - 1] == '-') result++;
	cout << result;
}

int main()
{
	freopen("b.txt", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		eval();
		cout << endl;
	}
		
	return 0;
}

