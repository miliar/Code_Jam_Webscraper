//https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int MinimumMoves(string s)
{
	if(s=="+") return 0;
	if(s=="-") return 1;
	if(s[0]==s[1]) return MinimumMoves(s.substr(1));
	return MinimumMoves(s.substr(1))+1;
}
int main()
{
	int t;
	cin >> t;
	int attempt=0;
	while(attempt!=t)
	{
		attempt++;
		string s;
		cin >> s;
		cout << "Case #" << attempt << ": "<< MinimumMoves(s) << endl;
	}
	return 0;
}