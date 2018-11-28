#include <iostream>  
using namespace std;
void main() {
	int t, k, c, s;
	cin >> t;
	for (int i = 1; i <= t; ++i) 
	{
		cin >> k >> c >> s;  // read n and then m.
		cout << "Case #" << i << ": ";
		if (c == 1)
		{
			for (int j = 1; j < k; ++j)
				cout << j << " ";
			cout << k << endl;
		}
		else
		{
			for (int j = 1; j < k; ++j)
				cout << j + k * (j - 1) << " ";
			cout << k * k << endl;
		}
		
	}
}