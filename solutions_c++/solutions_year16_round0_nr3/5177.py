#include <iostream>  
using namespace std;
void main() {
	int t, n, m;
	cin >> t;  
	for (int i = 1; i <= t; ++i) {
		cin >> n >> m;  // read n and then m.
		cout << "Case #" << i << ":" << endl;
		int arr[11];
		for (int j = 0; j < m; ++j)
		{	
				for (int kk = 0; kk < 11; ++kk)
					arr[kk] = 0;
				int ii = 0, r = 0;
				int num = j;
				while (num != 0)
				{
					r = num % 2;
					arr[ii++] = r;
					num /= 2;
				}
				std::cout << 1;
				for (int kk = n / 2 - 2; kk >= 0; --kk)
					std::cout << arr[kk] << arr[kk];
				std::cout << "1 3 2 5 2 7 2 3 2 11" << std::endl;
			
		}
	}
}