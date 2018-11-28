#include <bits/stdc++.h>
typedef long long LL;
using namespace std;









int main() {
	int n; cin >> n;
	for(int i = 1; i <= n; ++i){
		int k,c,s; cin >> k >> c >> s;

		std::cout << "Case #" << i << ":";
		if(s<k) cout << " IMPOSSIBLE" << endl;
		else{
		for(int j = 1; j <= k; ++j)
			std::cout << " " << j;
		
		std::cout << endl;
		}
	}


}
