#include <iostream>
#include <algorithm>
using namespace std;

struct test_case{
	double p[201];
	double sel[201];
	int n, k;
	
	double prob[201];
	
	double calcp(){
		for(int i=0; i<=k; i++) prob[i] = 0;
		prob[0] = 1;
		for(int x=0; x<k; x++){
			for(int s=k; s>0; s--){
				prob[s] = prob[s]*(1-sel[x]) + prob[s-1]*sel[x];
			}
			prob[0] *= 1-sel[x];
			
			//~ for(int i=0; i<=k; i++) cerr << prob[i] << ' '; cerr << endl;
		}
		return prob[k/2];
	}
	
	void solve(){
		cin >> n >> k;
		double ans = 0;
		for(int i=0; i<n; i++) cin >> p[i];
		sort(p, p+n);
		for(int i=0; i<=k; i++){
			for(int x=0; x<i; x++) sel[x] = p[x];
			for(int x=0; x<k-i; x++) sel[k-x-1] = p[n-x-1];
			ans = max(ans, calcp());
			//~ ans = calcp();
			//~ for(int i=0; i<k; i++) cerr << sel[i] << ' '; cerr << " -> " << ans << endl;
		}
		std::cout.precision(8);
		cout << fixed << ans;
	}
};

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		test_case s = {};
		s.solve();
		cout << endl;
	}
	return 0;
}
