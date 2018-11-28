#include<bits/stdc++.h>
using namespace std;

string s, tmp, res;
int main(){
	int tc;
	cin >> tc;
	for (int t = 1 ; t <= tc; t++){
		cin >> tmp;
		s = tmp;
		bool status = false;
		int balik = 0;
		int move = 0;
		while(!status){
			move++;
			status = true;
			balik = 0;
			char patokan = s[0];
			//cout << s << endl;
			for (int i = 0; i < s.length(); i++){
				if (s[i] != patokan){
					status = false;
					balik = i;
					break;
				} 
			}	
			res = "";
			if (balik > 0){
				for (int i = balik - 1; i >= 0; i--){
					if (s[i] == '+') res += "-"; else res += "+";
				}
			}	
			//cout << balik << endl;
			for (int i = 0; i < balik; i++){
				s[i] = res[i];
			}
		}
		cout << "Case #" << t << ": ";
		if (tmp == "-") cout << "1" << endl; else
		{
			bool haha = true;
			for (int i = 0 ; i < tmp.length(); i++) if (tmp[i] == '-') haha = false;
			if (s[0] == '-') move++;
			if (haha) cout << 0 << endl; else cout << move - 1 << endl;
		}
	}
	return 0;
}
