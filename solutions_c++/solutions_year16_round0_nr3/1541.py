#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <set>
#include <string>
#include <iomanip>
 
using namespace std;
 
int numBits(int n)
{
	int a = 2;
	int i = 1;

	while (a < n) {
		a = a*2;
		i++;
	}

	return i;
}

void incr(string &s)
{
	int n = s.length();

	for (int i = n-1; i >= 0; i--) {
		if (s[i] == '0') {
			s[i] = '1';
			return;
		}
		s[i] = '0';
	}
}

long long base(string &s, int k)
{
	long long val = 0;
	long long a = 1;
	int n = s.length();

	for (int i = n-1; i >= 0; i--) {
		if (s[i] == '1') 
			val += a;
		a = a * k;
	}

	return val;
}

int main()
{

	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {

		int N, J;
	
		cin >> N;
	
		cin >> J;
	
		int num = numBits(J);
	
	   cout << "Case #" << i+1 << ": " << endl;
	
		string s(num, '0');
	
		for (int j = 0; j < J; j++) {
			if (j > 0)
				incr(s);
	
			int diff = (N - (2 * (num+2)));
	
			string s2 = string(1, '1') + s + string(1, '1');
			if (diff > 0)
				s2 += string(diff, '0');
			s2 += string(1, '1') + s + string(1, '1');

			cout << s2 << " ";

			for (int k = 2; k <= 10; k++) {
				string s3 =  string(1, '1') + s + string(1, '1');
				cout << base(s3, k) << " ";
			}
			cout << endl;
		}
	}

	return 0;
}

	

