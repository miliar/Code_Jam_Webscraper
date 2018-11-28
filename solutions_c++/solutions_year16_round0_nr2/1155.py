#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

#define PII       pair<int,int>
#define all(c)    c.begin(),c.end()
#define sz(c)     (int)c.size()
#define clr(c)    c.clear()
#define pb        push_back
#define mp        make_pair
#define cin(x)    scanf("%d",&x)
#define MOD		1000000007
#define EPS		1E-10

ifstream fin("B-large.in");
ofstream fout("B-temp.out");

string REV(string str, int pos)
{
	reverse(str.begin() , str.begin() + pos + 1);
	for(int i = 0; i <= pos; i++)
		if(str[i] == '+')
			str[i] = '-';
		else
			str[i] = '+';
	return str;
}

int greedy(string s)
{
	while(sz(s) && s.back() == '+')
		s.pop_back();
	if(sz(s) == 0) return 0;
	int ret = 1;
	s.pop_back();
	for(int i = 0; i < sz(s); i++)
		if(s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	ret += greedy(s);
	return ret;
}

int main()
{
	int t;
	fin >> t;
	for(int i = 1; i <= t; i++)
	{
		fout << "Case #" << i << ": ";
		string s;
		fin >> s;
		fout << greedy(s) << "\n";
	}
	return 0;
}