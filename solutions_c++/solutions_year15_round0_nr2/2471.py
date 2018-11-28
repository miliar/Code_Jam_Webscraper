#include <bits/stdc++.h>

using namespace std;
vector<int> p;

int main(){
	int T; cin >> T;
	for (int t=1; t <= T; t++){
		p.clear();
		int d; cin >> d;
		int mx = 0;
		for (int i = 0; i < d; i++){
			int a; cin >> a;
			p.push_back(a);
			mx=max(mx,a);
		}
		int mn = mx;
		for (int i = 1; i <= mx; i++){
			int curr_ans = i; 
			for (int j = 0; j < p.size(); j++){
				if (p[j] > i){
					//cout << p[j] << " " << i << " added " << ((p[j]-1)/i) << endl;
					curr_ans += ((p[j]-1)/i);
				}
			}
			//cout << "cap " << i << " ans:" << curr_ans << endl;
			mn=min(mn,curr_ans);
		}
		cout << "Case #" << t << ": " << mn << endl;
	}

	return 0;
}
