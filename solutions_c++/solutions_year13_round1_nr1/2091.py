#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int t;
	unsigned long long r, p;
	unsigned long long ans;
	cin >> t;
	for(int j = 1; j <= t; j++){
		cin >> r >> p;
		ans = 0;
		unsigned long long men[2];
		for(int i = 1;; i += 2){
			men[0] = (r + i - 1) * (r + i - 1);
			men[1] = (r + i) * (r + i);
			if(p >= men[1] - men[0]){
				p -= men[1] - men[0];
				ans++;
			}
			else{
				break;
			}
		}
		
		cout << "Case #" << j << ": " << ans << endl;
	}
	return 0;
}

		
		
