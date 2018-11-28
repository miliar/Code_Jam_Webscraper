#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <stack>
#include <utility>

using namespace std;

vector <int> vv;
	

int main(){
	int T;
	freopen("B-large.in", "r+", stdin);
	cin >> T;
	int D;

	for(int t = 1; t <= T; t++){
		cin >> D;
		int maxElement = 0;
		
		vv.clear();
		vv.resize(D);

		for(int i = 0; i < D; i++){
			cin >> vv[i];
			maxElement = max(vv[i], maxElement);
		}

		sort(vv.rbegin(), vv.rend());

		int ans = maxElement;
		for(int i = 1; i <= maxElement; i++){
			int res = 0;
			for(int j = 0; j < (int) vv.size(); j++){
				if(i > vv[j]) continue;
				int w;
				if(vv[j] % i == 0)
					w = (vv[j] / i) - 1;
				else
					w = vv[j] / i;
				
				res += w;
			}
			ans = min(ans, res + i);

		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;	
}