#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <ctime>
#include <vector>
#include <algorithm>
#include <ctime>
#include <set>
#include <map>
using namespace std;

int sum[80005], sum2[80005];

map<char, int> _hash;
int imap[5][5];


/*
int main()
{
	//C-small-attempt0.in
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, L, X;
	cin >> T;
	map<char, int> _hash;
	_hash['1'] = 1, _hash['i'] = 2, _hash['j'] = 3, _hash['k'] = 4;
	int imap[5][5];
	imap[1][1] = 1, imap[1][2] = 2, imap[1][3] = 3, imap[1][4] = 4;
	imap[2][1] = 2, imap[2][2] = -1, imap[2][3] = 4, imap[2][4] = -3;
	imap[3][1] = 3, imap[3][2] = -4, imap[3][3] = -1, imap[3][4] = 2;
	imap[4][1] = 4, imap[4][2] = 3, imap[4][3] = -2, imap[4][4] = -1;
	int index = 1;
	while (T--)
	{
		cin >> L >> X;
		string line;
		cin >> line;
		string str = "";
		for (int i = 1; i <= X; ++i)str.append(line);
		int sz = str.size();
		sum[0] = _hash[str[0]];
		sum2[sz - 1] = _hash[str[sz - 1]];
		for (int i = 1; i < sz; ++i)
		{
			if (sum[i - 1] < 0)sum[i] = (-1) * imap[-sum[i - 1]][_hash[str[i]]];
			else sum[i] = imap[sum[i - 1]][_hash[str[i]]];

			if (sum2[sz - i] < 0)sum2[sz - i - 1] = (-1) * imap[_hash[str[sz - i - 1]]][-sum2[sz - i]];
			else sum2[sz - i - 1] = imap[_hash[str[sz - i - 1]]][sum2[sz - i]];
		}
		if (sum[sz - 1] != -1)
		{
			cout << "Case #" << index++ << ": NO" << endl;
		}
		else
		{
			bool hasans = false;
			for (int i = 0; i < sz; ++i)
			{
				if (sum[i] == 2)
				{
					for (int j = i + 2; j < sz; ++j)
					{
						if (sum2[j] == 4)
						{
							hasans = true;
							break;
						}
					}
					if (hasans)break;
				}
			}
			if(hasans)cout << "Case #" << index++ << ": YES" << endl;
			else
			{
				cout << "Case #" << index++ << ": NO" << endl;
			}
		}
	}
	return 0;
}

*/

typedef long long int64;

void calc_small(string &str, int &index)
{
	int sz = str.size();
	sum[0] = _hash[str[0]];
	sum2[sz - 1] = _hash[str[sz - 1]];
	for (int i = 1; i < sz; ++i)
	{
		if (sum[i - 1] < 0)sum[i] = (-1) * imap[-sum[i - 1]][_hash[str[i]]];
		else sum[i] = imap[sum[i - 1]][_hash[str[i]]];

		if (sum2[sz - i] < 0)sum2[sz - i - 1] = (-1) * imap[_hash[str[sz - i - 1]]][-sum2[sz - i]];
		else sum2[sz - i - 1] = imap[_hash[str[sz - i - 1]]][sum2[sz - i]];
	}
	if (sum[sz - 1] != -1)
	{
		cout << "Case #" << index++ << ": NO" << endl;
	}
	else
	{
		bool hasans = false;
		for (int i = 0; i < sz; ++i)
		{
			if (sum[i] == 2)
			{
				for (int j = i + 2; j < sz; ++j)
				{
					if (sum2[j] == 4)
					{
						hasans = true;
						break;
					}
				}
				if (hasans)break;
			}
		}
		if (hasans)cout << "Case #" << index++ << ": YES" << endl;
		else
		{
			cout << "Case #" << index++ << ": NO" << endl;
		}
	}
}
int main()
{
	//C-small-attempt0.in
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, L;
	int64 X;
	cin >> T;
	_hash['1'] = 1, _hash['i'] = 2, _hash['j'] = 3, _hash['k'] = 4;
	imap[1][1] = 1, imap[1][2] = 2, imap[1][3] = 3, imap[1][4] = 4;
	imap[2][1] = 2, imap[2][2] = -1, imap[2][3] = 4, imap[2][4] = -3;
	imap[3][1] = 3, imap[3][2] = -4, imap[3][3] = -1, imap[3][4] = 2;
	imap[4][1] = 4, imap[4][2] = 3, imap[4][3] = -2, imap[4][4] = -1;
	int index = 1;
	while (T--)
	{
		cin >> L >> X;
		string str;
		cin >> str;
		if (X < 8)
		{
			string str2 = "";
			for (int i = 1; i <= X; ++i)str2.append(str);
			calc_small(str2, index);
		}
		else
		{
			string str2 = str + str + str + str;
			int sz = str2.size();
			sum[0] = _hash[str2[0]];
			sum2[sz - 1] = _hash[str2[sz - 1]];
			for (int i = 1; i < sz; ++i)
			{
				if (sum[i - 1] < 0)sum[i] = (-1) * imap[-sum[i - 1]][_hash[str2[i]]];
				else sum[i] = imap[sum[i - 1]][_hash[str2[i]]];

				if (sum2[sz - i] < 0)sum2[sz - i - 1] = (-1) * imap[_hash[str2[sz - i - 1]]][-sum2[sz - i]];
				else sum2[sz - i - 1] = imap[_hash[str2[sz - i - 1]]][sum2[sz - i]];
			}
			
			if (((sum[(2*str.size()) - 1] == -1) && ((((X >> 1) & 1) == 0) || (X&1)!=0)) || 
				((sum[(str.size()) - 1] == -1) && ((X & 1) == 0)) || sum[str.size()-1]==1)
			{
				cout << "Case #" << index++ << ": NO" << endl;
			}
			else
			{
				bool hasans = false;
				for (int i = 0; i < sz; ++i)
				{
					if (sum[i] == 2)
					{
						hasans = true;
						break;
					}
				}
				if (hasans)
				{
					hasans = false;
					for (int i = 0; i < sz; ++i)
					{
						if (sum2[i] == 4)
						{
							hasans = true;
							break;
						}
					}
				}
				
				if (hasans)cout << "Case #" << index++ << ": YES" << endl;
				else
				{
					cout << "Case #" << index++ << ": NO" << endl;
				}
			}
		}
		
	}
	return 0;
}