#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

bool fine(vector<char>& vc){
	int l = (int)vc.size();
	for(int i=0;i<l;i++){
		if(vc[i] == '-')return false;
	}
	return true;
}

void flip(vector<char>& vc, int c , bool b){
	if(b){
		for(int i=0;i<c;i++)vc[i]='+';
	}
	else{
		for(int i=0;i<c;i++)vc[i]='-';
	}
}

int main(){
	int t;
	cin >> t;
	for(int j=1;j<=t;j++){
		string str;
		cin >> str;
		cout << "Case #"<<j<<": ";

		int l = (int)str.length();
		vector<char> s;
		for(int i=0;i<l;i++)s.push_back(str[i]);
		
		int count = 0;
		while(!fine(s)){
			if(s[0] == '+'){
				int rev=0;
				while(rev<l && s[rev]=='+' )++rev;
				flip(s,rev,0);
			}
			else{
				int rev=0;
				while(rev<l && s[rev]=='-' )++rev;
				flip(s,rev,1);
			}
			++count;
		}
		cout << count << endl;
	}
	return 0;
}
