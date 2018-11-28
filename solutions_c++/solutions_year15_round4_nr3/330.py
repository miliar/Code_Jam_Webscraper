#include<bits/stdc++.h>
using namespace std;

map<string,int> dict;
int w[4096],n,m;
vector<int> u[1234];
int main(){
	int T;
	cin >> T;
	for(int ti=1;ti<=T;++ti){
		cin >> n;cin.get();
		dict.clear();m=0;
		cout << "Case #" << ti << ": ";
		for(int i=0;i<n;++i){
			static char buf [12345];
			cin.getline(buf,12345);
			u[i].clear();
			string tmp;
			for(istringstream iss(buf);iss >> tmp;){
				if(!dict.count(tmp))
					dict[tmp]=m++;
				u[i].push_back(dict[tmp]);
			}
			//for(int x:u[i])cout << x << " "; cout << endl;
		}
		int ans=m;
		for(int z=1;z<(1<<n);z+=4){
			fill(w,w+m,0);
			for(int i=0;i<n;++i){
				int k=1<<(z>>i&1);
				for(int v:u[i])w[v]|=k;
			}
			ans=min<int>(ans,count(w,w+m,3));
		}
		cout << ans << endl;
	}
}
