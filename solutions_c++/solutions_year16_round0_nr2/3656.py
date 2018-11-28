#include<iostream>
#include<string>

using namespace std;

typedef long long ll;

ll count_flips(string s, char c) {
	int n = s.length();
	int p = n-1;
	while (p>=0 && s[p]==c)	p--;
	if (p<0)	return 0;
	else if (c=='-')	return 1+count_flips(s.substr(0,p+1),'+');
	else 	return 1+count_flips(s.substr(0,p+1),'-');
}

int main()
{
	ios::sync_with_stdio(false);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		string s; cin >> s;
/*		int n = s.length();
		int p = n-1;
		ll flips = 0;
		//string result(n,'+');
		while(p>=0) {
			if (s[p]!='+'){
				if (s[0]=='+') {
					flips++;
					s[0] = '-';
				}
				string temp = "";
				int j = p;
				while (j>=0) {
					if (s[j]=='-')	temp+='+';
					else temp += '-';
					j--;
				}
				s = temp + s.substr(p+1);
				flips++;
//				cout << s << "\n";
			}
			p--;
		}*/
		cout << count_flips(s,'+') << "\n";
	}
}
