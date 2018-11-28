#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t; cin >> t;
	for (int ti = 1; ti <=t; ti++) {
		int result = 1001;
		int d; cin >> d;
		vector<int> H (d);
		for (int i = 0; i<d; i++)
			cin >> H[i];		
		for (int pi = 1; pi <=1000; pi++){
			int turns = pi;
			for (int i=0; i<d; i++)
				turns += max((H[i]-1) / pi, 0);
			result = min(result, turns);
		}
		printf ("Case #%d: %d\n", ti, result);
	}
}
