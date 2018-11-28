#include<iostream>
using namespace std;

int count(string s){
	int l = s.length();
	if(l == 0)return 0;
	else{
		int c = 0;
		for(int i = 0; i < l-1; i++){
			if(s[i] != s[i+1])c++;
		}
		if(s[l-1] == '-')c++;
		return c;
	}
}

int main(){
	int n;
	string s;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> s;
		cout << "Case #" << i+1 << ": " << count(s) <<endl;
	}
	//system("pause");
	return 0;
}
