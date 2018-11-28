#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	//cout <<"hey" << endl;
	for(int caseNum=1;caseNum<=T;caseNum++) {
		vector<int>a; int asize;
		cin >> asize;
		for(int i=0;i<asize;i++) {
			int num; cin >> num;
			a.push_back(num);
		}

		int min1= 0;
		int rate = 0;
		for(int i=0;i+1<asize;i++) {
			if (a[i+1]<a[i]){
				min1 +=  abs(a[i+1] - a[i]);
				rate = max(rate, abs(a[i+1]-a[i]));
			}

		}
		int min2=0;
		for(int i=0;i+1<asize;i++) {
			min2+=min(rate,a[i]);
		}
		cout << "Case #"<<caseNum<<": "<<min1<<" " << min2 << "\n";
	}
	return 0;
}