#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int count(vector<string> v){
	if (v.size() == 0) return 0;
	sort(v.begin(), v.end());
	int tot = 0;
	tot += v[0].size();
	for (int i = 1; i<v.size(); i++){
		int j;
		for (j = 0; j<v[i-1].size() && j<v[i].size(); j++)
			if (v[i-1][j] != v[i][j]) break;
		tot += v[i].size()-j;
	}
	return tot;
}
int  maxnode;
int sum;
string a[10];
int kind[10];
int n, m;
void dfs(int k){
	if (k == m){
		int tot = 0;
		for (int i = 0; i<n; i++){
			vector<string> v;
			for (int j = 0; j<m; j++) if (kind[j] == i) v.push_back(a[j]);
			if (v.size() == 0){
				tot = -999999;
				break;
			}
			tot += count(v);
		}
		if (tot > maxnode){
			maxnode = tot;
			sum = 1;
		}else if (tot == maxnode){
			sum++;
		}
		return ;
	}

	for (int i = 0; i<n; i++){
		kind[k] = i;
		dfs(k+1);
	}
}
int main(){
	int T, cas = 0;
	for (cin>>T; T--;){
		cout<<"Case #"<<++cas<<": ";
		sum = 0;
		maxnode = -1;
		cin>>m>>n;
		for (int i = 0; i<m; i++) cin>>a[i];
		dfs(0);
		cout<<maxnode+n<<' '<<sum<<endl;
	}
	return 0;
}



