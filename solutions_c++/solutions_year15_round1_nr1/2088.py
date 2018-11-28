#include <iostream>
#include <vector>

using namespace std;

int minimum(int a, int b){
	if (a < b) return a;
	return b;
}

int main(){

	int t, n, min1, min2, diff, rate, min, buffer;
	vector<int> v;
	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		v.clear();
		min1 = 0;
		min2 = 0;
		rate = 0;
		cin >> n;
		for(int nn = 0; nn < n; nn++){
			cin >> buffer;
			v.push_back(buffer);
		}
		if(v[0] < v[1]) rate = v[0] - v[1];
		for(int nn = 1; nn < n; nn++){
			diff = v[nn-1] - v[nn];
			if(v[nn] <= v[nn-1]){
				min1 += diff;
			}
			if(diff > rate) rate = diff;
		}
		for(int nn = 0; nn < n; nn++){
			min2 += minimum(rate, v[nn-1]);
		}
		cout << "Case #" << tt << ": " << min1 << " " << min2 << endl;
	}
	return 0;
}