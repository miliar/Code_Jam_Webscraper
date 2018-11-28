#define _CRT_SECURE_NO_WARNINGS 
#include <iostream>
#include<string>

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		string s;
		cin >> s;
		int col = 0;
		bool fl = false;
		int a = 0;
		while((a < s.size()) || fl){
			if ((a == s.size()) && fl){
				for (int j = 0; j < s.size(); j++){
					if (s[j] == '-') s[j] = '+';
					else if (s[j] == '+') s[j] = '-';
				}
				a = 0;
				col++;
				fl = false;
			}
			if ((s[a] == '+') && (!fl) && (a < s.size())){
				a++;
			}
			if ((s[a] == '-') && (a < s.size())){
				fl = true;
				a++;
			}
			if ((s[a] == '+') && (fl) && (a < s.size())){
				for (int j = 0; j < a; j++){
					if (s[j] == '-') s[j] = '+';
					else if (s[j] == '+') s[j] = '-';
				}
				a = 0;
				col++;
				fl = false;
			}
		}
		cout << "Case #" << i << ": " << col << '\n';
	}
	return 0;
}
