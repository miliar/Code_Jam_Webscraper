#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int T, k=0, n, c1, c2;
	cin >> T;
	while(T--) {
		cin >> n;
		vector<double> noemi(n);
		vector<double> ken(n);
		for(int i=0;i<n;i++)
			cin >> noemi[i];
		for(int i=0;i<n;i++)
			cin >> ken[i];
		std::vector<double> v(n);
		sort(ken.begin(), ken.end());
		sort(noemi.begin(), noemi.end());
		copy(noemi.begin(), noemi.end(), v.begin());
		// for decitfull war

		c1 = 0;
		for(int i=0;i<ken.size();i++) {
			for(int j=0;j<v.size();j++) {
				if(v[j] > ken[i]) {
					c1++;
					v.erase(v.begin()+j);
					break;
				}
			}
		}

		// for war only

		c2 = 0;
		for(int i=0;i<noemi.size();i++) {
			for(int j=0;j<ken.size();j++) {
				if(ken[j] > noemi[i]) {
					c2++;
					ken.erase(ken.begin()+j);				
					break;
				}
			}
		}
		c2 = n-c2;

		// print

		cout << "Case #" << ++k << ": " << c1 << " " << c2 << "\n";
	}
	return 0;
}