#include <iostream>
using namespace std;

int T;
int d;
int p[1010];

int main() {
	cin >> T;
	
	for (int lacase = 1; lacase <= T; lacase++) {
		cin >> d;
		
		for (int i = 0; i < d; i++)
			cin >> p[i];
		
		int res = 1000;
		for (int largest = 1; largest <= 1000; largest++) {
			int cur = largest;
			
			for (int i = 0; i < d; i++)
				if (largest < p[i])
					cur += (p[i]-1)/largest;
			
			res = min(res, cur);
		}
		
		cout << "Case #" << lacase << ": " << res << "\n";
	}
	
	return 0;
}
