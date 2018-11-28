#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

long long solve(){
	int D;
	cin >> D;
	vector<int> P(D);
	for(int i=0; i<D; i++){
		cin >> P[i];
	}
	sort(P.begin(), P.end());

	int max_ = P.back();
	long long ans = 1e9;
	for(int k=1; k<=max_; k++){
		long long tmp = k;
		for(int i=0; i<D; i++){
			if(P[i] <= k) continue;
			if(P[i] % k == 0){
				tmp += P[i]/k - 1;
			}else{
				tmp += P[i]/k;
			}
		}
		ans = min(ans, tmp);
	}

	return ans;

}

int main(){
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}