#include <iostream>
#include <string>
#include <vector>

using namespace std;

string s;

void flip(int x)
{
	vector<char> v;
	for(int i=0;i<=x;i++)
	{
		if (s[i]=='-') v.push_back('+');
		else v.push_back('-');
	}
	int j=0;
	while(v.size()>0)
	{
		s[j]=v.back();
		v.pop_back();
		j++;
	}
}

long long solve()
{
	long long res = 0;
	if (s.size()==0) return -1;
	int i = s.size()-1;
	int j=0;
	while(i>=0)
	{
		if (s[i]=='-')
		{
			if (s[0]=='-')
			{
				flip(i);
				res++;
			}
			else
			{
				j=0;
				while(s[j]=='+')
				{
					s[j]='-';
					j++;
				}
				flip(i);
				res += 2;
			}
		}
		i--;
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	for(int z=0;z<T;z++)
	{
		cin >> s;
		cout << "Case #" << z+1 << ": " << solve() << endl;
	}
}