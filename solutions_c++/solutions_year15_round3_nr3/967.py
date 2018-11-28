#include <bits/stdc++.h>
using namespace std;

int C,D,V;
vector<int>vec;

int doSim() {
	int used[50] = {0};
	for(int i=0;i<vec.size();i++) {
		for(int j=V;j>=0;j--) {
			if (used[j]) {
				if (j+vec[i]<=V)
					used[j+vec[i]]=true;
			}
		}
		used[vec[i]]=true;
	}
	for(int i=1;i<=V;i++) {
		if (!used[i]) return i;
	}
	return -1;
}

int main() {
	int T; cin >> T;
	for(int caseNum=1; caseNum<=T; caseNum++) {
		cin >> C >> D >> V;
		vec.clear();
		for(int i=0;i<D;i++) {
			int n; cin >> n; vec.push_back(n);
		}
		int ans = 0;
		while (true) {
			int c = doSim();
			if (c==-1) {
				cout << "Case #"<<caseNum<<": " << ans << endl;break;
			}
			//cout << " added " <<c << endl;
			vec.push_back(c);
			ans++;
		}
	}
}