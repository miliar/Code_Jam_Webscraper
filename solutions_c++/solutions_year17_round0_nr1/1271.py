#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

bool use[1005];
int main(){
	ifstream fin("A-large.in");
	ofstream fout("output.out");
	int T,tt = 1;
	fin >> T;
	while(T--){
		string s;
		int i, len,k;
		fin >> s >> k;
		//cout << s<<endl;
		len = s.length();
		int ans = 0, tmp = 0;
		memset(use,0,sizeof(use));
		for(i = 0;i <= len - k ; i++){
			if(i >= k) tmp -= use[i-k];
			if(s[i] == '-') {
				if(tmp % 2 == 0) {
					ans++;
					tmp++;
					use[i] = 1;
				}
			}
			else if(s[i] == '+'){
				if(tmp%2 == 1){
					ans++;
					tmp++;
					use[i] = 1;
				}
			}
		}
		bool fg = 1;
		for(i = len - k+1;i < len; ++i){
			if(i >= k) tmp -= use[i-k];
			if(s[i] == '-' && tmp%2 == 0) fg = 0;
			else if(s[i] == '+' && tmp%2 == 1) fg = 0;
		}
		fout <<"Case #" << tt++ <<": ";
		if(fg == 0) fout << "IMPOSSIBLE\n";
		else fout <<ans <<endl;
	}
	
	
	return 0;
}