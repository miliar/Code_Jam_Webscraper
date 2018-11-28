#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int compare(string s1, string s2) {
	for (int i = 0; i < s1.length(); i++)
		if (s1[i] < s2[i])
			return 1;
		else if (s1[i] > s2[i])
			return 0;
	return 0;
}

int main() {
	int n;
	fin>>n;
	for (int i = 1; i <= n; i++) {
		string s;
		string ans="";
		fin>>s;
		for (int j = 0; j < s.length(); j++) {
			string s1 = s[j]+ans;
			string s2 = ans+s[j];
			if (!compare(s1, s2))
				ans = s[j] + ans;
			else ans = ans + s[j];
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
}