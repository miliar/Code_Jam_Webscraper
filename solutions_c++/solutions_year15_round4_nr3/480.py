#include <bits/stdc++.h>

#define debug(a)

using namespace std;

int n;

vector<string> getline()
{
	vector<string> v;
	string s;
	char c;
	scanf(" %c", &c);
	s += c;
	while(scanf("%c", &c) != EOF)
	{
		if(c == '\n')
			break;
		if(c == ' ')
		{
			if(s != "")
				v.emplace_back(s);
			s = "";
		}
		else
			s += c;
	}
	if(s != "")
		v.emplace_back(s);
	return v;
}

vector<string> zdanie[205];

map<string, int> maski;

int licz(int m)
{
	int wyn = 0;
	for(auto & x : maski)
		if((m & x.second) == x.second || (m & x.second) == 0)
			wyn++;
	return (int) maski.size() - wyn;
}

int przyp()
{
	maski.clear();
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		zdanie[i] = getline();
		for(auto & s : zdanie[i])
			maski[s] |= (1 << i);
		debug(
			printf("%d:", i);
			for(auto & s : zdanie[i])
				printf(" %s", s.c_str());
			printf("\n");
		)
	}
	debug(
		for(auto & x : maski)
		{
			printf("%s: ", x.first.c_str());
			for(int i = 0; i < n; i++)
				if(x.second & (1 << i))
					printf("1");
				else
					printf("0");
			printf("\n");
		}
	)
	int wyn = n * 1000;
	for(int i = 0; i < (1 << (n - 2)); i++)
		wyn = min(wyn, licz((i << 2) + 1));
	return wyn;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, przyp());
	return 0;
}
