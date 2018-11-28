#include <bits/stdc++.h>

using namespace std;

string numb[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string s;
int t;

bool look(string s, char c){
	for(int j = 0;j<s.length();j++){
		if(s[j]==c)
			return true;
	}
	return false;
}

int main(){
	cin>>t;
	char c;
	int k = t;
	while(t){
		string num = "";
		cin>>s;
		sort(s.begin(), s.end());
		reverse(s.begin(), s.end());
		while(s[0]=='Z'){
			num = num+to_string(0);
			for(int i=0; i<numb[0].length(); i++){
				c = numb[0][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
				
		}
		while(s[0]=='X'){
			num = num+to_string(6);
			for(int i=0; i<numb[6].length(); i++){
				c = numb[6][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
		}

		while(s[0]=='W'){
			num = num+to_string(2);
			for(int i=0; i<numb[2].length(); i++){
				c = numb[2][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
		}
		while(s[0]=='V'){
			if(look(s,'S')){
				num = num+to_string(7);
				for(int i=0; i<numb[7].length(); i++){
				c = numb[7][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}

			}
			else{
				num = num+to_string(5);
				for(int i=0; i<numb[5].length(); i++){
				c = numb[5][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
			}
			
		}
		while(s[0]=='U'){
			num = num+to_string(4);
			for(int i=0; i<numb[4].length(); i++){
				c = numb[4][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
		}
		while(s[0]=='T'){
			if(look(s,'G')){
			num = num+to_string(8);
			for(int i=0; i<numb[8].length(); i++){
				c = numb[8][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
		}
			else{
				num = num+to_string(3);
				for(int i=0; i<numb[3].length(); i++){
				c = numb[3][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
			}
		}
		
		while(s[0]=='O'){
			num = num+to_string(1);
			for(int i=0; i<numb[1].length(); i++){
				c = numb[1][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
		}
		while(s[0]=='N'){
			num = num+to_string(9);
			for(int i=0; i<numb[9].length(); i++){
				c = numb[9][i];
				for(int j = 0;j<s.length();j++){
					if(s[j]==c){
						s.erase(j,1);
						break;
					}
				}
			}
		}
		
		sort(num.begin(), num.end());
		cout<<"Case #"<<k-t+1<<": "<<s<<num<<endl;
		t--;
	}
	
}
