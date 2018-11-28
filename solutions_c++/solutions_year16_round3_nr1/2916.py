#include<bits/stdc++.h>
using namespace std;

typedef pair<int,char> ic;

bool major(vector<int> v) {
	int n=v.size(), total=0, mx=0;
	for (int i=0; i<n; i++) {
		total+=v[i],
		mx=max(mx,v[i]);
	}
	cout << mx << "/" << total << endl;

	if(2*mx>total) return true;
	return false;
}

bool check(vector<int> v, vector<string> &ret) {
	int sz=ret.size();
	for (int i=0; i<sz; i++) {
		char a=ret[i][0], b=ret[i][1];
		v[a-'A']--; v[b-'A']--;
		if(major(v)) return false;
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t; cin>>t;
	for (int c=1; c<=t; c++) {
		int n; cin>>n;
		vector<ic> x;
		vector<int> v;
		for (int i=0; i<n; i++) {
			int cur; cin>>cur;
			x.push_back(make_pair(cur, 'A'+i));
			v.push_back(cur);
		}

		vector<string> ret;
		while(1) {
			sort(x.begin(), x.end(), greater<ic>());
			ic a=x[0], b=x[1];
			if(a.first==1) {
				int val=0;
				for (int i=0; i<x.size(); i++) {
					if(x[i].first) val++;
				}

				for (int i=0; i<val-2; i++) {
					string cur; cur+=x[i].second;
					if(x[i].first) {
						ret.push_back(cur);
						x[i].first--;
					}
				}

				string cur; cur+=x[val-2].second; cur+=x[val-1].second;
				x[val-2].first--; x[val-1].first--;
				ret.push_back(cur);
			} else {
				string cur;
				if(a.first) {
					cur+=a.second;
					x[0].first--;
				}
				if(b.first) {
					cur+=b.second;
					x[1].first--;
				}
				if(cur.empty()) break;
				ret.push_back(cur);
			}
		}

//		if(!check(v, ret)) cout << "WRONG" << endl;

		int sz=ret.size();
		cout << "Case #" << c << ": ";
		for (int i=0; i<sz; i++) {
			if(i) cout << " ";
			cout << ret[i];
		}
		cout << endl;
	}
	return 0;
}
