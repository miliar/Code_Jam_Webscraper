#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <stack>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int dp[1000100];

#define cin fin
#define cout fout

string rev(string s , int x){
	stack<char> ss;
	for(int i = 0 ; i <= x ; ++i){
		if(s[i] == '-')
			ss.push('+');
		else
			ss.push('-');
	}

	for(int i = 0 ; i <= x ; ++i){
		s[i] = ss.top();
		ss.pop();
	}
	return s;
}

int main(){
	int t;
	cin >> t;
	for(int o = 0 ; o < t ; ++o){
		string s;
		cin >> s;

		int ans = 0;

		while(true){
			//cout << s << endl;
			int ii = 0;
			while(ii < s.size() && s[ii] == '+') ++ii;
			if(ii == s.size()) break;
			if(ii != 0) ++ans;
			s = rev(s , ii - 1);
			//cout << "1 : " << s << endl;

			for(int i = s.size() - 1 ; i >= 0 ; --i){
				if(s[i] == '-'){
					//cout << i << endl;
					s = rev(s , i);
					++ans;
					break;
				}
			}
			//cout << "2 : " << s << endl;
		}

		cout << "Case #" << o + 1 << ": ";
		cout << ans << endl;
	}		

	return 0;
}