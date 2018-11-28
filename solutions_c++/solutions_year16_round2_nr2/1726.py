#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

vector < pair<int, pair<int, int> > > p;

int myabs(int a)
{
	return a > 0 ? a : -a;
}

string translate(int i, int num)
{
	char buf[5];
	int cot = 1;
	if (num != 0)
	{
		cot = (int)log10((double)num) + 1;
	}

	switch (i)
	{
	case 1:
		switch (cot)
		{
		case 1:
			sprintf(buf, "%d", num);
			break;
		case 2:
			break;
		case 3:
			break;
		}
		break;
	case 2:
		switch (cot)
		{
		case 1:
			sprintf(buf, "0%d", num);
			break;
		case 2:
			sprintf(buf, "%d", num);
			break;
		case 3:
			break;
		}
		break;
	case 3:
		switch (cot)
		{
		case 1:
			sprintf(buf, "00%d", num);
			break;
		case 2:
			sprintf(buf, "0%d", num);
			break;
		case 3:
			sprintf(buf, "%d", num);
			break;
		}
		break;
	}
	return buf;
}

bool match(char* str,int num)
{
	string buf;
	
	buf = translate(strlen(str), num);
	
	for (int i = 0; str[i]; i++)
	{
		if (str[i] != buf[i])
		{
			if (str[i] != '?')
			{
				return false;
			}
		}
	}
	return true;
}


int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		p.clear();
		char a[20] = { 0, }, b[20] = { 0, };
		//string ar,br;
		scanf("%s%s", a, b);
		int c = strlen(a);
		if (string(a) == "???" && string(b) == "???")
		{
			p.push_back(make_pair(0, make_pair(0, 0)));
		}
		else
		{
			int res = 1;

			for (int i = 0; i < c; i++)
			{
				res *= 10;
			}

			for (int i = 0; i < res; i++)
			{
				for (int j = 0; j < res; j++)
				{
					if (match(a, i) && match(b, j))
					{
						p.push_back(make_pair(myabs(i - j), make_pair(i, j)));
					}
				}
			}
		}
		sort(p.begin(), p.end());
		string ar = translate(c,(*p.begin()).second.first);
		string br = translate(c,(*p.begin()).second.second);
		
		printf("Case #%d: %s %s\n", i, ar.c_str(),br.c_str());
	}
	return 0;
}