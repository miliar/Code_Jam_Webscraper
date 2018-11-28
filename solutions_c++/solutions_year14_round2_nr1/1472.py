#include <bits/stdc++.h>

using namespace std;

string get(string s){
	string ans;
	int sz = s.size();
	for(int i = 0 ; i < sz ; ++i){
		if(i == sz - 1)ans += s[i];
		else if(s[i] != s[i + 1])ans += s[i];
	}
	return ans;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.in","w",stdout);
	int T;
	int k = 1;
	cin >> T;
	while(T--){
		int res = 0;
		int n;
		cin >> n;
		vector<string> V(n);
		for(int i = 0 ; i < n ; ++i)cin >> V[i];
		string comp = get(V[0]);
		bool bad = 0;
		for(int i = 1 ; i < n ; ++i){
			if(comp != get(V[i])){
				bad = 1;
				break;
			}
		}
		if(bad){
			cout << "Case #" << k << ": " << "Fegla Won" << endl;
			++k;
			continue;
		}

		vector<int> ind(n);
		int real = comp.size();
		for(int i = 0 ; i < real ; ++i){
			vector<int> num(n);
			for(int j = 0 ; j < n ; ++j){
				int now = V[j].size();
				int ctr = 0;
				for(int &l = ind[j] ; l < now ; ++l){
					ctr++;
					if(l == now - 1){
						num[j] = ctr;
					}
					else if(V[j][l] != V[j][l + 1]){
						num[j] = ctr;
						++l;
						break;
					}
				}
			}

			int mini = 1000000;
			for(int j = 0 ; j < n ; ++j){
				int diff = 0;
				for(int l = 0 ; l < n ; ++l){
					if(l == j)continue;
					diff += abs(num[j] - num[l]);
				}
				mini = min(mini , diff);
			}
			res += mini;
		}
		cout << "Case #" << k << ": " << res << endl;
		++k;
	}
	return 0;
}
