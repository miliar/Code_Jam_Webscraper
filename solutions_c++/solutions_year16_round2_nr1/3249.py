#include <bits/stdc++.h>
#define MAX 10e9+7

using namespace std;
typedef unsigned long long ull;

string number[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int size = 1;

string remove(string s, int i){
	char c;
	int len = number[i].length();
	for(int j=0; j<len; j++){
		c = number[i][j];
		for(int k=0; k<s.length(); k++){
			if(c==s[k]){
				//cout << c;
				s.erase(k,size);
				break;
			}
		}
	}
	return s;
}

bool look(string s, char c){
	for(int i=0; i<s.length(); i++){
		if(c==s[i]){
			return true;
		}
	}
	return false;
}

string check(string s){
	int output[10];
	string out = "";
	int count;
	int l = 0;
	string temp;
	sort(s.begin(),s.end());
	reverse(s.begin(),s.end());
	while(s[0]=='Z'){
		s = remove(s,0);
		out = out+to_string(0);
	}
	while(s[0]=='X'){
		s = remove(s,6);
		out = out+to_string(6);
	}
	while(s[0]=='W'){
		s = remove(s,2);
		out = out+to_string(2);
	}
	while(s[0]=='V'){
		if(look(s,'S')){
			s = remove(s,7);
			out = out+to_string(7);
		}
		else{
			s = remove(s,5);
			out = out+to_string(5);
		}
	}
	while(s[0]=='U'){
		s = remove(s,4);
		out = out+to_string(4);
	}
	while(s[0]=='T'){
		if(look(s,'G')){
			s = remove(s,8);
			out = out+to_string(8);
		}
		else{
			s = remove(s,3);
			out = out+to_string(3);
		}
	}
	while(s[0]=='O'){
		s = remove(s,1);
		out = out+to_string(1);
	}
	while(s[0]=='N'){
		s = remove(s,9);
		out = out+to_string(9);
	}
	cout << s;
	return out;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.io","w",stdout);
	int test,i=1;
	string s;
	string ans;
	cin >> test;
	while(i<=test){
		cin >> s;
		cout << "Case #" << i << ":" << " ";
		ans = check(s);
		sort(ans.begin(),ans.end());
		cout << ans;
		// for(int j=0; j<10 && ans[j]!=-1; j++){
		// 	cout << ans[j];
		// }
		cout << endl;
		i++;
	}
	return 0;
}