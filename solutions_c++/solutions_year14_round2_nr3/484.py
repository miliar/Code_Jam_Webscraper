#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <random>
#include <set>
#include <sstream>
#include <cassert>

using namespace std;

typedef long long ll;

bool doable(const vector<int>& per, const vector<vector<int>>& g){
	vector<int> stack;
	stack.push_back(per[0]);
	for(int i=1;i<int(per.size());++i){
		int v = per[i];
		while(find(begin(g[stack.back()]), end(g[stack.back()]), v) == end(g[stack.back()])){
			if(stack.size()==1)
				return false;
			else
				stack.pop_back();
		}
		stack.push_back(v);
	}
	return true;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int T;
	cin >> T;
	for(int icase=1;icase<=T;++icase){
		cout << "Case #" << icase << ": ";
		int n, m;
		cin >> n >> m;
		vector<int> zip(n);
		for(int i=0;i<n;++i)
			cin >> zip[i];

		string res(n*5, '9');


		vector<vector<int>> g(n);
		for(int i=0;i<m;++i){
			int a, b;
			cin >>a >>b;
			--a; --b;
			g[a].push_back(b);
			g[b].push_back(a);
		}

		vector<int> per(n);
		for(int i=0;i<n;++i)
			per[i]=i;

		do{
			if(doable(per, g)){
				ostringstream tmp;
				for(int i=0;i<n;++i)
					tmp << zip[per[i]];
				res = min(res, tmp.str());
			}
		}while(next_permutation(begin(per), end(per)));
		cout << res << endl;
	}
}