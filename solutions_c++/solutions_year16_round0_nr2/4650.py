#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

typedef long long BigInt;

BigInt pancakes_flip(const string &s)
{
	BigInt n_flips = 0;
	char c = s[0];
	BigInt n = s.size();
	
	for (int i=1;i<n;i++){
		if (s[i]!=s[i-1]){ n_flips++; c=s[i]; }
	}
	if (c=='-') n_flips++;
	
	return n_flips;
}

int main()
{
	BigInt T;
	string s;
	
	cin >> T;
	for (BigInt c=1;c<=T;c++){
		cin >> s;
		
		BigInt n_flips = pancakes_flip(s);
		
		cout << "Case #" << c << ": " << n_flips << endl;
	}
	
	return 0;
}
