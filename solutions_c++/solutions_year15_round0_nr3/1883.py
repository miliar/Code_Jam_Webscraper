#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<vector<int>> table{ {0,1,2,3}, {1,0,3,2}, {2,3,0,1}, {3,2,1,0} };
vector<vector<int>> sign{ {1,1,1,1}, {1,-1,1,-1}, {1,-1,-1,1}, {1,1,-1,-1} };

int Map(char c)
{
	switch (c)
	{
	case 'i':return 1;
	case 'j':return 2;
	case 'k':return 3;
	}
}
int main()
{
	int T,X;
	int L;
	string str;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> L >> X>>str;
		int total = L*X;
		int j = 0, k = 0;
		int val = Map(str[j++]), s = 1;
		++k;
		if (j == L)j = 0;
		while ((k < total) && !(val == 1 && s == 1))
		{
			s = s * sign[val][Map(str[j])];
			val = table[val][Map(str[j])];
			++k;
			++j;
			if (j == L) j = 0;
		}
		if (k == total)
		{
			cout << "Case #" << i + 1 << ": NO" << endl;
			continue;
		}
		val = Map(str[j++]);
		++k;
		if (j == L) j = 0;
		while ((k < total) && !(val == 2 && s == 1))
		{
			s = s * sign[val][Map(str[j])];
			val = table[val][Map(str[j])];
			++k;
			++j;
			if (j ==L) j = 0;
		}
		if (k == total)
		{
			cout << "Case #" << i + 1 << ": NO" << endl;
			continue;
		}
		val = Map(str[j++]);
		++k;
		if (j == L) j = 0;
		while ((k < total))
		{
			s = s * sign[val][Map(str[j])];
			val = table[val][Map(str[j])];
			++k;
			++j;
			if (j == L) j = 0;
		}
		if (!(val == 3 && s == 1))
		{
			cout << "Case #" << i + 1 << ": NO" << endl;
			continue;
		}
		cout << "Case #" << i + 1 << ": YES" << endl;
	}
}