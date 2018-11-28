#include <iostream>
#include <vector>
#include <algorithm>
#define int long long

using namespace std;

int n;
int maxi = 0;
vector<int> na;

main() {
	ios_base::sync_with_stdio(0);
	int z; cin >> z;
	int q = z;
	while(z--) {
		na.resize(0);
		int wyn;
		maxi = 0;
		cin >> n;
		na.resize(n);
		for(auto &i :  na) { cin >> i;  maxi = max(maxi,i);} 
		wyn = maxi;
		sort(na.begin(), na.end());
		reverse(na.begin(), na.end());
		for(int i = 1; i < maxi+1; ++i) {
			int lokalnywyn = i;
			for(int x = 0;(x < na.size()) && na[x] > i; ++x) {
				int k = na[x];
				if(k % i == 0) 
					lokalnywyn += k/i-1;
				else 	
					lokalnywyn += k/i;
			}
			wyn = min(wyn,lokalnywyn);
		}
		cout << "Case #" << (q-z) << ": " << wyn << endl;
	}
}
