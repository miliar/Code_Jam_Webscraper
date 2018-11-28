#include <iostream>
#include <string>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=0; i<t; ++i){
		string s;
		int c=1;
		cin >> s;
		for(int j=1; j<s.size(); ++j){
			if(s[j]!=s[j-1]) c++;
		}
		if((c%2==1 && s[0]=='+') || (c%2==0 && s[0]=='-')) c--;
		cout << "Case #" << i+1 << ": " << c << endl;
	}
	return 0;
}