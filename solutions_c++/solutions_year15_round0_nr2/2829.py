#include <vector>
#include <iostream>
#include <list>
#include <cmath>
#include <unordered_map>
#include <algorithm>

using namespace std;

int T;
vector<vector<int>> input;

void getInput() {
	cin>>T;

	for (int i=0; i<T; i++) {
		int D;
		cin>>D;
		vector<int> c;
		input.push_back(c);
		for (int j=0; j<D; j++) {
			int p;
			cin>>p;
			input[i].push_back(p);
		}
		
	}
}

int main () {
	getInput();
	
	for (int i=0; i<T; i++) {
		vector<int> v = input[i];
		int mx = 0;

		for (int x=0; x<v.size(); x++) {
			mx = max(mx, v[x]);
		}
		int ans = 0x7ffffff;
		for (int j=1; j<=mx; j++) {
			int temp = 0;
			for (int k=0; k<v.size(); k++) {
				if (v[k] > j && (v[k]%j == 0)) {
					temp += v[k]/j - 1;
				}
				else if (v[k] > j && (v[k]%j != 0)) {
					temp += v[k]/j;
				}
			}
			ans = min(ans, temp+j);
		}
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}

	return 0;
}
