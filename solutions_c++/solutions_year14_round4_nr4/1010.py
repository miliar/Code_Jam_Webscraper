#include <bits/stdc++.h>
using namespace std;
int tcs, n, m, nways[100000000], ans;
vector<string> s;

int compute(vector<vector<string> > st){
	int ts = n;
	for(int i=0;i<n;i++){
		if(st[i].size() == 0) return 0;
		set<string> pfs;
		for(int j=0;j<st[i].size();j++){
			for(int k=1;k<=st[i][j].length();k++){
				pfs.insert(st[i][j].substr(0, k));
			}
		}
		ts += pfs.size();
	}
	return ts;
}


void recursive(int index, vector<vector<string> > stored){ 
	if(index == m){
		int res = compute(stored);
		nways[res]++;
		ans = max(ans, res);
		return;
	}
	
	for(int j=0;j<n;j++){
		vector<vector<string> > k(stored);
		k[j].push_back(s[index]);
		recursive(index + 1, k);
	}
}

int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%i%i", &m, &n);
		s.clear();
		for(int i=0;i<m;i++){
			char buf[10000];
			scanf("%s", buf);
			s.push_back(string(buf));
		}
		ans = 0;
		memset(nways, 0, sizeof nways);
		vector<vector<string> > t;
		t.assign(10, vector<string>());
		recursive(0, t);
		printf("Case #%i: %i %i\n", tc, ans, nways[ans]);
	}
}