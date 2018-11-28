#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
using namespace std;

char winner(char c1, char c2)
{
	if (c1 > c2) swap(c1, c2);
	if (c1 == 'P')
	{
		if (c2 == 'S') return c2;		
	}
	return c1;
}

bool check(vector<char> mas)
{
	while (mas.size() > 1)
	{
		vector<char> tmp(mas.size() / 2);
		bool b = false;
		for (int i = 0; i < mas.size()/2; ++i)
		{
			if (mas[i * 2] == mas[i * 2 + 1])
			{
				b = true;
				break;
			}
			tmp[i] = winner(mas[i * 2], mas[i * 2 + 1]);
		}
		if (b)
			break;
		mas.assign(tmp.begin(), tmp.end());
	}
	if (mas.size() == 1)
		return true;
	else return false;
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int n, T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		cout<<"Case #"<<i + 1<<": ";
		long long r,p,s;
		cin>>n>>r>>p>>s;
		vector<char> mas;
		for (int l = 0; l < p; ++l)
			mas.push_back('P');
		for (int l = 0; l < r; ++l)
			mas.push_back('R');
		for (int l = 0; l < s; ++l)
			mas.push_back('S');
		while (!check(mas) && next_permutation(mas.begin(), mas.end()));
		if (check(mas))
		{
			for (int i1 = 0; i1 < mas.size(); ++i1)
				cout<<mas[i1];
			cout<<endl;
		}
		else cout<<"IMPOSSIBLE\n";

	}
	
	return 0;
}