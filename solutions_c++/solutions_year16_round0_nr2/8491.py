#include <iostream>
using namespace std;

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int x = 1; x <= t; x++){
		string s;
		cin >> s;
		int l = s.length();
		int i = 0;
		int count = 0;
		if(s[i] == '+')i++;
		else{
			count++;
			i++;
		}
		while(i < l){
			if(s[i]==s[i-1])i++;
			else if(s[i]=='+')i++;
			else if(s[i]=='-'){
				count += 2;
				i++;
			}
		}
		cout << "Case #" << x << ": " << count << endl;
	}
}