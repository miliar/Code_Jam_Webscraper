#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;


int main() {
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE<=T; TCASE++) {
		int n;
		cin >> n;
		cout << "Case #" << TCASE << ": ";
		
		if(n == 0) {
			cout << "INSOMNIA\n";
			continue;
		}
		
		int i=1;
		vector<bool> found(10, false);
		
		while(find(found.begin(), found.end(), false) != found.end() ) {
			string cur = to_string(i*n);
			
			for(auto c : cur)
				found[c-'0'] = true;
			i++;
		}
		
		cout << (i-1)*n << '\n';

	}
	
	return 0;
}



















