//Author: net12k44
#include <bits/stdc++.h>
using namespace std;
int n;
const int limit = 1000000 + 5;
map<string,int> id;
int cnt[2][limit];
vector<int> s[250];
int res;

void visit(int i, int diff = 0){
	if (diff > res) return;
	if (i==n){
		if (res > diff) res = diff;
	} else
	for(int k = 0; k < 2; ++k)
	if (i>=2 || k==i){
		for(auto c: s[i]){
			cnt[k][c]++;
			if (cnt[k][c]==1 && cnt[1^k][c]) diff++;
		}
		visit(i+1, diff);
		for(auto c: s[i]){
			cnt[k][c]--;
			if (cnt[k][c]==0 && cnt[1^k][c]) diff--;
		}
	}
}

void solve(){
	scanf("%d\n",&n); 
	id.clear();
	memset(cnt, 0, sizeof cnt);
	for(int i = 0; i < n; ++i){
		s[i].clear();
		string tmp;
		getline(cin, tmp);
		stringstream ss(tmp);
		while (ss >> tmp) {
			int cur = id.size();
			if (id.find(tmp) == id.end())
				id[tmp] = cur;
			s[i].push_back(id[tmp]);
		}
	//	for(auto c: s[i]) cout << c << " "; cout << endl;
	}
	
	res = 1000000000;
	visit(0);	
	printf("%d\n",res);
}

int main(){
	int test; scanf("%d",&test);
	for(int t=1; t<=test; ++t){
		printf("Case #%d: ",t);
		solve();
	}	
}
