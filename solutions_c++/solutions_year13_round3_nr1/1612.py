#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <fstream>

using namespace std;

bool isVowel(char c){
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

bool isOK(string s, int n)
{
	int ncons = 0;
	
	for(unsigned i = 0; i < s.size();++i){
		if(isVowel(s[i]))
			ncons = 0;
		else
			++ncons;
		if(ncons == n)
			return true;
	}
	return false;
}

long long solve(string s, int n)
{
	long long ret = 0;
	
	for(unsigned i = 0; i < s.size(); ++i)
		for(unsigned len = n; len <= s.size();++len)
			if(i + len <= s.size())
				if(isOK(s.substr(i, len), n))
					++ret;
					
	return ret;
}

int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	
	int tno;
	in >> tno;
	for(int t = 1; t <= tno; ++t){
		string s;
		int n;
		in >> s >> n;
		out << "Case #" << t << ": " << solve(s, n) << endl;
	}
	
	return 0;
}
