#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i=0; i<T; ++i){
		int N;
		int ans=0;
		bool flag=false;
		cin >> N;
		vector<string> str(N);
		vector<vector<pair<char,int> > > count(N);
		for(int j=0; j<N; ++j){
			cin >> str[j];
			for(int k=0; k<str[j].size(); ++k){
				if(k==0||(k!=0&&str[j][k]!=str[j][k-1])) count[j].push_back(pair<char,int>(str[j][k],1));
				else ++count[j][count[j].size()-1].second;
			}
			if(j!=0&&count[j].size()!=count[j-1].size()){
				flag=true;
				//cout << 11111 << endl;
			}
		}
		if(!flag){
			for(int j=0; j<count[0].size(); ++j){
				int sum=0;
				for(int k=0; k<N; ++k){
					if(k!=0&&count[k][j].first!=count[k-1][j].first){
						//cout << k << ' ' << j << endl;
						//cout << count[k][j].first << ' ' << count[k][j].second << endl << count[k-1][j].first << ' ' << count[k-1][j].second << endl;
						flag=true;
						//cout << 2222 << endl;
						break;
					}
					sum+=count[k][j].second;
				}
				if(flag) break;
				int tmp=0;
				for(int k=0; k<N; ++k) tmp+=abs(round(sum/N)-count[k][j].second);
				ans+=tmp;
			}
		}
		if(flag) cout << "Case #" << i+1 << ": Fegla Won\n";
		else cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
