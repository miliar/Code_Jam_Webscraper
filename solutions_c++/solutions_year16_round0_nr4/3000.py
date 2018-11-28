#include <iostream>
#include<algorithm>
#include<string>
#include<map>
#include<fstream>
#include <bitset>
#include <vector>

using namespace std;
/*
vector<pair<string, vector<int> > > v(50);
int r = 0;
bool fin = false;

void call(string st)
{
	string t = '1' + st + '1';
	v[r].first = t;
	for (int j = 2; j < 11; j++)
	{
		long long cnt = 0;
		for (int i = t.length()-1; i >=0; i--)
		{
			if (t[i] == '1')
				cnt += pow(j, t.length()-1 - i);
		}
		bool flag = false;
		int k = 2;
		for (k; k*k <= cnt; k++)
		{
			if (cnt%k == 0) {
				flag = true; break;
			}
		}
		if (flag && k>1)
			 v[r].second.push_back(k);
		else  break;
	}
	if (v[r].second.size() == 9)
		r++;
	else v[r].second.clear();
	if (r == 5)
		fin = true;
}

void rec(string s)
{
	if (fin)return;
	if (s.length() == 14) {
		call(s); return;
	}
	rec(s + '0');
	rec(s + '1');
}
*/
int main()
{
	ifstream inf;
	inf.open("D-small-attempt1.in", std::ifstream::in);
	ofstream outf;
	outf.open("out.txt", std::ofstream::out);
	int t; inf >> t;
	for (int i = 1; i <= t; i++)
	{
		int k, c, s; 
		inf >> k >> c >> s;
		outf << "Case #" << i << ": ";
		for (int y = 1; y <= k; y++)
			outf << y << " ";
		outf << endl;
	}
	return 0;
}
