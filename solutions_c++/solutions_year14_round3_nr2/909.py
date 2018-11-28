#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(){
	int tt;
	cin >> tt;
	for(int t = 1; t <= tt; t++){
		int n;
		bool inv = false;
		cin >> n;
		string s[101];
		int inmid[26];
		int strtype[101];
		int x[101];
		int ln = 0;
		for(int i = 0; i < 26; i++){
			inmid[i] = 0;
		}

		for(int i = 0; i < 101; i++){
			strtype[i] = 0;
		}
		for(int i = 0; i < n; i++){
			cin >> s[i];
			string sx = "";
			char ch = s[i][0];
			sx += ch;
			int j = 1, k = s[i].length()-1;
			while(j < s[i].length() && s[i][j] == ch){
				j++;
			}
			ch = s[i][s[i].length()-1];
			while(k >= 0 && s[i][k] == ch){
				k--;
			}
			if(k < j && ch == s[i][0]){//all same
				strtype[i] = 1;
			}
			else{
				strtype[i] = 2;
				for(; j <= k; j++){

					while(j <=k && s[i][j] == s[i][j-1])
						j++;
					sx += s[i][j];
					if(s[i][j] == s[i][0] || s[i][j] == s[i][s[i].length()-1]){
						inv = true;
						break;
					}
					else if(inmid[s[i][j]-'a']){
						inv = true;
						break;
					}
					else{
						inmid[s[i][j]-'a']++;
					}
				}
				sx += s[i][s[i].length()-1];
			}
			s[i] = sx;
			ln += s[i].length();
			x[i] = i;


		}
		long long ans = 0;
		if(!inv){
			do{
				inv = false;
				string ls;
				ls = "";
				for(int i = 0; i < n; i++){
					ls = ls + s[x[i]];
				}
				ls[ln] = 0;
				int i = 0;
				while(i < ln){
					char ch = ls[i];
					while(i < ln && ls[i] == ch){
						i++;
					}
					for(int j = i; j < ln; j++){
						if(ls[j] == ch){
							inv = true;
							break;
						}
					}
					if(inv)
						break;
				}
				if(!inv)
					ans++;
			}
			while(next_permutation(x, x+n));
		}
		cout << "Case #" << t << ": " << ans%1000000007 << endl;
	}
	return 0;
}

