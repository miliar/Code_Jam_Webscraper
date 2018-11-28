#include<bits/stdc++.h>
using namespace std;

bool isgreater(string s1, string s2){
	for(int i = 0; i < s1.length(); i++){
		if(s1[i] > s2[i]){
			return true;
		}

			if(s1[i] < s2[i]){
				return false;
			}
	}

	return false;
}

string s;

string createBest(int pos1, int pos2){

	if(pos1 > pos2){
		return "";
	}

	int mx = -1;
	for(int i = pos1; i <= pos2; i++){
		mx = max(mx, s[i] - 'A');
	}

	string res = "";
	bool flag = false;
	for(int i = pos1; i <= pos2; i++){
		string tmp = "";
		if((s[i]-'A') == mx){
			tmp = s[i] + createBest(pos1, i-1) + createBest(i+1, pos2);
			if(flag  && isgreater(tmp, res)){
				res = tmp;
			}
			else{
				flag = true;
				res = tmp;
			}
		}
	}

	return res;

}

int main(){
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		printf("Case #%d: ", z);
		cin >> s;
		string res = "";
		res = res + s[0];
		//cout << res << endl;
		for(int i = 1; i < s.size(); i++){
			if(s[i] >= res[0])
				res = s[i] + res;
			else{
				res = res + s[i];
			}
		}
		cout << res << endl;
	}
return 0;
}