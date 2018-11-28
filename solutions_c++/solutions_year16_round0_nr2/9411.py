#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int moves = 0;
		string a;
		cin >> a;
		for(int j = a.length() - 1; j >= 0; j--)
		{
			if(a[j] == '-' && a[j+1] != '-')
				moves++;
			if(a[j] == '+' && a[j+1] == '-')
				moves++;
		}
		cout << "Case #" << i+1 << ": " << moves << endl;
	}
	return 0;
}
