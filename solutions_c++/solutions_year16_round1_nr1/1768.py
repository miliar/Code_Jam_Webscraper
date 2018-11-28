#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string last_word (string s)
{
	string new_s;
	for (int i=0; i<s.length(); i++)
	{
		if (new_s.length()==0)
			new_s+=s[i];
		else if (s[i]>=new_s[0])
			new_s=s[i]+new_s;
		else
			new_s+=s[i];
	}
	return new_s;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		string s;
		cin >> s;
		printf ("Case #%d: %s\n", i+1, last_word(s).c_str());
	}
}
