#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <string>


using namespace std;

char S[100000];

struct result
{
	int sign;
	char c;
	result()
	{
		c = '1';
		sign = 1;
	}
	result(char c, int sign)
	{
		this->c = c;
		this->sign = sign;
	}
}R[10000][10000];

char C[10000][10000];
char SN[10000][10000];

struct state
{
	vector<int> index;
	result res;
	state(){}
	state(result r) : res(r)
	{
	}
};
map<char, map<char, result>> table;

void solve();
int main()
{
	table['1']['1'] = result('1', 1);
	table['1']['i'] = result('i', 1);
	table['1']['j'] = result('j', 1);
	table['1']['k'] = result('k', 1);
	table['i']['1'] = result('i', 1);
	table['i']['i'] = result('1', -1);
	table['i']['j'] = result('k', 1);
	table['i']['k'] = result('j', -1);
	table['j']['1'] = result('j', 1);
	table['j']['i'] = result('k', -1);
	table['j']['j'] = result('1', -1);
	table['j']['k'] = result('i', 1);
	table['k']['1'] = result('k', 1);
	table['k']['i'] = result('j', 1);
	table['k']['j'] = result('i', -1);
	table['k']['k'] = result('1', -1);

	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
}
void solve2()
{
	int l, x;
	scanf("%d %d", &l, &x);
	scanf("%s", S);
	int count = l*x;
	for (int i = 0; i < count; i++)
	{
		char c = S[i % l];
		C[i][i] = c;
		SN[i][i] = 1;
		for (int j = i + 1; j < count; j++)
		{
			c = S[j % l];
			result tr = table[C[i][j - 1]][c];

			C[i][j] = tr.c;
			SN[i][j] = SN[i][j - 1] * tr.sign;
		}
	}
	for (int i = 0; i < count; i++)
	{
		if (C[0][i] == 'i' && SN[0][i] == 1)
		{
			for (int j = i + 1; j < count; j++)
			{
				if (C[i + 1][j] == 'j' && SN[i + 1][j] == 1)
				{
					if (C[j + 1][count - 1] == 'k' && SN[j + 1][count - 1] == 1)
					{
						printf("YES");
						return;
					}
				}
			}
		}
	}
	printf("NO");
}
void solve()
{
	solve2();
	return;
	int l, x;
	int ic=0, jc=0, kc=0;
	char lookFor[] = "ijk";
	scanf("%d %d", &l, &x);
	for (int i = 0; i < l; i++)
	{
		char c = getc(stdin);
		if (c == '\r' || c == '\n')
		{
			i--;
			continue;
		}
		if (c == 'i')
			ic++;
		if (c == 'j')
			jc++;
		if (c == 'k')
			kc++;

		S[i] = c;
	}
	if (!(ic*jc) && !(ic*kc) && !(jc*kc))
	{
		printf("NO");
		return;
	}
	//scanf("%s", S);
	int count = l * x;
	int index = 0;
	result r('1', 1);
	std::vector<state> s;
	bool found = false;
	while (1)
	{
		char c = S[index % l];
		if (c == '-')
		{
			r.sign *= -1;
			index++;
			c = S[index % l];
		}
		result t = table[r.c][c];
		r.c = t.c;
		r.sign *= t.sign;
		bool bHandled = false;
		if (r.c == lookFor[s.size()] && r.sign == 1)
		{
			if (index == count - 1 && r.c == 'k' && s.size() == 2)
			{
				found = true;
				break;
			}
			if (r.c != 'k' && index != count - 1)
			{
				state ts(r);
				//ts.index.push_back(index + 1);
				s.push_back(ts);
				r.c = '1';
				r.sign = 1;
				bHandled = true;
			}
		}
		if (!bHandled && index != count - 1)
		{
			if (r.c == '1' && r.sign == 1 && s.size())
			{
				s[s.size() - 1].index.push_back(index + 1);
			}
			else if (r.c == 'k' && r.sign == 1 && s.size() == 2)
			{
				s[0].index.push_back(index + 1);
			}
		}
		if (index == count - 1)
		{
			vector<state>::iterator it;
			while (1)
			{
				if (!s.size())
					break;
				it = s.end() - 1;
				if ((*it).index.size())
				{
					break;
				}
				s.pop_back();
			}
			if (!s.size())
				break;
			//s.pop_back();
			r = (*it).res;
			index = (*it).index[0];
			(*it).index.erase((*it).index.begin());
		}
		else
		{
			index++;
		}
	}
	if (found)
		printf("YES");
	else
		printf("NO");
}