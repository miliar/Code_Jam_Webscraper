#include<iostream>
#include<vector>

using namespace std;


int main(){
	int T; cin >>T;
	for(int t=0;t<T; ++t){
		int m; cin >> m;
		string s;cin >> s;
		int ov=0;
		int ret=0;
		for(int i=0; i<=m; ++i){
			int at=s[i]-'0';
			if(at==0) continue;
			if(ov>=i) ov+=at;
			else{
				ret+=(i-ov);
				ov+=at+(i-ov);
			}
		}
		cout << "Case #"<<t+1<<": "<< ret << endl;
	}
	return 0;
}
