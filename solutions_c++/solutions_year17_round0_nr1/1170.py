#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

typedef unsigned uint;
using namespace std;
static const char nl = '\n';

void flip(string& s,uint index,uint K)
{
	for(uint i = index;i < index + K;++i)
	{
		switch(s[i])
		{
			case '+':
				s[i] = '-';
				break;
			case '-':
				s[i] = '+';
				break;
		}
	}
}

int go(string& s,uint index,uint K)
{
	if(index >= s.length()) return 0;
	uint pancakesRemaining = s.length() - index;
	if(pancakesRemaining < K)
	{
		for(uint i = index;i < s.length();++i)
		{
			if(s[i] == '-') return -1;
		}
		return 0;
	}
	if(s[index] == '+')
	{
		return go(s,index+1,K);
	}
	flip(s,index,K);
	int retVal = go(s,index+1,K);
	if(retVal >= 0)
	{
		retVal = 1 + retVal;
	}
	return retVal;
}


int go()
{
	string s;
	uint K;
	cin >> s >> K;
	return go(s,0,K);
}

int main(int argc,char* argv[])
{
	ios_base::sync_with_stdio(false);
	uint T;
	cin >> T;
	for(uint i = 0;i < T;++i)
	{
		int r = go();
		cout << "Case #" << (i+1) << ": ";
		if(r >= 0)
		{
			cout << r;
		}
		else
		{
			cout << "IMPOSSIBLE";
		}
		cout << nl;
	}
	return 0;
}
