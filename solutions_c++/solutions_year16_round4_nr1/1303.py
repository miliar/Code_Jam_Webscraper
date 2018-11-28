#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int a[1000];
int temp[1000];
char b[5000][5000];
string ss[5000];
string tt[5000];

string xx[100];

string genString(char c, int numRound)
{
	b[0][0] = c;
	int cc = 1;
	for (int i = 1; i < numRound; i++)
	{
		for (int j = 0; j < cc; j++)
		{
			b[i][j * 2] = xx[b[i - 1][j]][0];
			b[i][j * 2 + 1] = xx[b[i - 1][j]][1];
			//cout << b[i][j * 2] << endl;
		}
		cc *= 2;
	}
	for (int i = 0; i < cc; i++)
	{
		ss[i] = "";
		ss[i] += b[numRound - 1][i];
	}
		//ss[i] = "" + b[numRound - 1][i];
	
	for (int i = numRound - 2; i >= 0; i--)
	{
		cc /= 2;
		for (int j = 0; j < cc; j++)
			if (ss[j * 2].compare(ss[j * 2 + 1]) > 0)
			{
				tt[j] = ss[j * 2 + 1] + ss[j * 2];
			}
			else
				tt[j] = ss[j * 2] + ss[j * 2 + 1];
		for (int j = 0; j < cc; j++)
			ss[j] = tt[j];
	}
	return ss[0];
}

bool countAndCompare(const string &s)
{
	memset(temp, 0, sizeof(temp));
	for (int i = 0; i < s.length(); i++)
	{
		temp[s[i]]++;
	}
	if (temp['R'] != a['R'] || temp['P'] != a['P'] || temp['S'] != a['S'])
		return false;
	return true;
}

int main()
{
	freopen("d:\\A-large.in", "r", stdin);
	freopen("d:\\output.txt", "w", stdout);
	xx['R'] = "SR";
	xx['S'] = "PS";
	xx['P'] = "PR";
	//cout << genString('R', 3) << endl;
	int oo;
	scanf("%d", &oo);
	for (int o = 0; o < oo; o++)
	{
		printf("Case #%d: ", o + 1);
		int N;
		scanf("%d", &N);
		scanf("%d", &a['R']);
		scanf("%d", &a['P']);
		scanf("%d", &a['S']);
		string s1 = genString('P', N + 1);
		string s2 = genString('S', N + 1);
		string s3 = genString('R', N + 1);
		//cout << "==" << s1 << s2 << s3 << endl;
		vector<string> res;
		res.clear();
		if (countAndCompare(s1))
			res.push_back(s1);
		if (countAndCompare(s2))
			res.push_back(s2);
		if (countAndCompare(s3))
			res.push_back(s3);
		if (res.size() == 0) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		string dhvan = res[0];
		for (int i = 1; i < (int)res.size(); i++)
			if (dhvan.compare(res[i]) > 0)
				dhvan = res[i];
		cout << dhvan << endl;
	}
}