#include<vector>
#include<string>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<stack>
#include<set>
#include<map>

using namespace std;
map<char,int> charMap;
void mul(int&p, char a, int& sign)
{
	if(p == 1)
		p = charMap[a];
	else if(p == 2)
	{
		if(a == 'i')
		{
			p = 1;
			sign *= -1;
		}
		if(a == 'j')
		{
			p = 4;
		}
		if(a == 'k')
		{
			p = 3;
			sign *= -1;
		}
	}
	else if(p == 3)
	{
		if(a == 'i')
		{
			p = 4;
			sign *= -1;
		}
		if(a == 'j')
		{
			p = 1;
			sign *= -1;
		}
		if(a == 'k')
		{
			p = 2;
		}
	}
	else if(p == 4)
	{
		if(a == 'i')
		{
			p = 3;
		}
		if(a == 'j')
		{
			p = 2;
			sign *= -1;

		}
		if(a == 'k')
		{
			p = 1;
			sign *= -1;
		}
	}
}
bool canFormK(string& s)
{
	int p = charMap[s[0]];
	int sign = 1;
	for(int i=1;i<s.size();++i)
	{
		mul(p, s[i], sign);
	}
	if(p == charMap['k'] && sign == 1)
		return true;
	return false;
}
bool canFormJ(string& s)
{
	int p = charMap[s[0]];
	int sign = 1;
	for(int i=1;i<s.size();++i)
	{
		if(p == charMap['j'] && sign == 1)
		{
			string subst = s.substr(i);
			if(canFormK(subst))
				return true;
			return false;
		}
		mul(p,s[i],sign);
	}
	return false;
}
bool canFormI(string& s)
{
	int p = charMap[s[0]];
	int sign = 1;
	for(int i=1;i<s.size();++i)
	{
		if(p == charMap['i'] && sign == 1)
		{
			string subst = s.substr(i);
			if(canFormJ(subst))
				return true;
			return false;
		}
		mul(p,s[i],sign);
	}
	return false;
}
int main()
{
	ifstream in("./input.txt");
	ofstream out("./output.txt");
	charMap['i'] = 2;
	charMap['j'] = 3;
	charMap['k'] = 4;
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
	int N;
	cin >> N;
	for (int t = 1; t <= N; ++t)
	{
		int l,x;
		cin>>l>>x;
		string s;
		string p =s;
		cin>>s;
		for(int i=0;i<x;++i)
			p += s;
		bool res = canFormI(p);
		string out;
		if(res)
			out = "YES";
		else 
			out = "NO";
		cout<<"Case #"<<t<<": "<<out<<endl;
	}
}