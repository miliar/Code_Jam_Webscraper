#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int a, b, k, count = 0;
		
		cin >> a >> b >> k;
		for (int x = 0; x < a; x++)
			for (int y = 0; y < b; y++)
				if ((x&y) < k) {
					count++;
				}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	
	return 0;
}