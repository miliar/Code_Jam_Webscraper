#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
#include <vector>

using namespace std;

int main(){
	int T,n, tmp;
	cin>>T;
	string s;
	int x=0;
	while(T--){
		unordered_map<int,int> mp;
		cin>>n;
		x++;
		for(int i=0;i<n*2-1;i++){
			for(int j=0;j<n;j++){
				cin>>tmp;
				mp[tmp]++;
			}
		}
		
		
		cout << "Case #"<<x<<":";
		vector<int> re;
		for(auto it=mp.begin();it!=mp.end();it++){
			if(it->second %2 !=0) re.push_back(it->first);
		}
		sort(re.begin(), re.end());
		for(int i=0;i<re.size();i++){
			cout<<" "<<re[i];
		}
		cout<<endl;
		
	}
	return 0;
}
