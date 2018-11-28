#include <iostream>
#include<algorithm>
#include<string>
#include<map>
#include<fstream>
#include <bitset>
#include <vector>

using namespace std;

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
	if (r == 50)
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

int main()
{
	ifstream inf;
	inf.open("B-large.in", std::ifstream::in);
	ofstream outf;
	outf.open("out.txt", std::ofstream::out);
	int t; inf >> t;
	int x, y;inf>>x>>y;
	for (int i = 1; i <= t; i++)
	{
		string s = "";
		rec(s);
		outf << "Case #" << i << ":" << endl;
		for (int j = 0; j < 50; j++)
		{
			outf << v[j].first << " ";
			for (int u = 0; u < 9; u++)
			{
				outf << v[j].second[u]<<" ";
			}
			outf << endl;
		}
	}
	return 0;
}
