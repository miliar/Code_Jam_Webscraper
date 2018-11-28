#include <iostream>
#include <map>
using namespace std;

map<int,int> mp;
map<int,int>::iterator it;

int main() {
	int T;
	cin>>T;
	int cs = 1;
	while(T--) {
		int n;
		cin>>n;
		int x;
		mp.clear();
		for(int i=0;i<2*n-1;i++) {
			for(int j=0;j<n;j++) {
				cin>>x;
				mp[x]++;
			}
		}
		cout<<"Case #"<<cs++<<": ";
		
		for(it = mp.begin(); it!=mp.end();it++) {
			if(it->second % 2) cout<<it->first<<" ";
		}
		cout<<endl;
	}
	// your code goes here
	return 0;
}