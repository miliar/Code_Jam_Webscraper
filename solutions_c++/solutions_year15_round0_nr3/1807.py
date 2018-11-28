#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

string s;
string ss;
int m, n;

class cool
{
	public:
	int sign;
	char c;

	cool(int sign, char c) {
		this->sign = sign;
		this->c = c;
	}

	cool()
	{
		cool(1, '1');	
	}
};

cool rules[300][300];
cool prefix[11000];
cool suffix[11000];

cool add(cool c1, cool c2)
{
	cool ret = rules[c1.c][c2.c];
	ret.sign *= c1.sign * c2.sign;

	return ret;
}

string solve()
{
	scanf("%d%d", &m, &n);

	cin >> ss;
	s = "1";
	int i, j;
	for(i = 0; i < n; i ++)
	{
		s += ss;
	}
	s += "1";

	prefix[0] = cool(1, '1');
	for(i = 1; i < s.size(); i ++)
	{
		prefix[i] = add(prefix[i-1], cool(1, s[i]));
	}
	suffix[s.size() - 1] = cool(1, '1');

	for(i = s.size() - 2; i >=0; i--)
	{
		suffix[i] = add(cool(1, s[i]), suffix[i+1]);
	}	

	for(i = 1; i < s.size() - 3; i++)
	{
		if(prefix[i].c != 'i' || prefix[i].sign != 1)
		{
			continue;
		}

		cool temp = cool(1, '1');
		for(j = i +1; j < s.size()-2; j++)
		{
			temp = add(temp, cool(1, s[j]));

			if(temp.c == 'j' && suffix[j + 1].c == 'k' && temp.sign == 1 && suffix[j+1].sign == 1)
			{
				return "YES";
			}
		}
	}

	return "NO";
}
int main ()
{
	char c1;
	rules['1']['1'] = cool(1, '1');
	for(c1 = 'i'; c1 <= 'k'; c1++)
	{
		rules['1'][c1] = rules[c1]['1'] = cool(1, c1);
		rules[c1][c1] = cool(-1, '1');
	}

	rules['i']['j'] = cool(1, 'k');
	rules['i']['k'] = cool(-1, 'j');
	rules['j']['k'] = cool(1, 'i');
	rules['j']['i'] = cool(-1, 'k');
	rules['k']['i'] = cool(1, 'j');
	rules['k']['j'] = cool(-1, 'i');

	int t; 
	scanf ("%d", &t);

	for(int i = 1; i <= t; i++)
	{
		printf("Case #%d: %s\n", i, solve().c_str());
	}

	return 0;
}