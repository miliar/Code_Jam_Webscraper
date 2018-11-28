#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main(){
	//ofstream out;
	//ifstream in;
	//in.open("B-large.in");
	//out.open("sample.out");
	int t;
	cin >> t;
	int j = 1;
	while (t--){
		string s;
		cin >> s;
		int ans = 0;
		char ch;
		if (s[s.length() - 1] == '-'){
			ans++;
			ch = '-';
		}
		else{
			ch = '+';
		}

		for (int i = s.length() - 2; i >= 0; i--){
			if (s[i] != ch){
				ans++;
				ch = s[i];
			}
		}
		cout << "Case #"<< j << ": "<< ans << "\n";
		j++;
	}
	//out.close();
	return 0;
}