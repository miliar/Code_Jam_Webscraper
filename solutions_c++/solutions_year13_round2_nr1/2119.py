#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int calc(int a, vector<int> &motes, int pos) {
	if(pos == motes.size()) {
		return 0;
	}
	if(a > motes[pos]) {
		return calc(a+motes[pos],motes,pos+1);
	} else {
		//delete
		int res = 1+calc(a,motes,pos+1);
		if(a > 1) {
			//create
			int res2 = 1+calc(a+a-1,motes,pos);
			if(res2 < res) return res2;
		}
		return res;
	}
}

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		int a,n;
		cin >> a >> n;
		vector<int> motes(n);
		for(int j = 0; j < n; ++j) {
			cin >> motes[j];
		}
		sort(motes.begin(),motes.end());
		int res = calc(a,motes,0);
		cout << "Case #" << i+1 << ": "<< res << endl;
	}
}