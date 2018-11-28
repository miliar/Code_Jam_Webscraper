#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;
ULLI y = 0;
void reverse_punk(string& str, LLI bot)
{
	string ret;
	for(LLI i=bot; i>=0; i--)
	{
		if(str[i] == '+')
			ret.push_back('-');
		else
			ret.push_back('+');
	}
	str.replace(0, bot+1, ret);
	y++;
}

int main(int argc, char** argv)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		y=0;
		string punk;
		cin >> punk;
		bool scorripiu;
		for(LLI k=0; k<punk.size(); k++)
		{
			scorripiu = (punk[k] == '+') ? true : false;
			if(!scorripiu)
			{
				if(punk.size() == 1)
				{
					reverse_punk(punk, k);
					continue;
				}
				if(k)
					reverse_punk(punk, k-1);
				bool altrimeno=true;
				while(altrimeno && k<punk.size())
				{
					k++;
					altrimeno = (punk[k] == '-') ? true : false;
				}
				reverse_punk(punk, k-1);
			}
		}
		cout << "Case #" << i+1 << ": " << y << endl;
	}
	return 0;
}
