#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;



int main(){
	int t;
	cin >> t;
	for(int i = 0; i< t; i++){
		int n;
		cin >> n;
		map<int,int> m;
		for(int j = 0; j < 2*n -1; j++){
			for(int k = 0; k < n; k++){
				int q;
				cin >> q;
				if(m.find(q)!=m.end())m[q]++;
				else m[q] = 1;
			}
		}
		map<int,int>::iterator it;
		vector<int> ans;
		ans.clear();
		for(it = m.begin(); it!=m.end(); it++ ){
			if(it->second%2 == 1)ans.push_back(it->first);
		}
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<i+1<<": "; 
		for(int i =0; i<ans.size();i++)cout << ans[i] << " ";
		cout << endl;
	}

	
	return 0;
}
