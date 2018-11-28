#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<algorithm>
#include<unordered_map>
using namespace std;

int testn;
int n, r, p, s;
vector<string> res;

int main()
{
	ifstream in("A-large.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");

	in >> testn;
	for (int test = 1; test <= testn; ++test) 
	{
		// input
		res.clear();
		in >> n >> r >> p >> s;

		string ss, temp; 
		string str = "PRS";
		for (int i = 0; i < 3; ++i)
		{
			ss = " ";
			ss[0] = str[i];
			
			for (int j = 0; j < n; ++j)
			{
				temp = "";
				int ssize = ss.size();
				for (int k = 0; k < ssize; ++k)
				{
					if (ss[k] == 'P')
						temp.append("PR");
					else if (ss[k] == 'R')
						temp.append("RS");
					else
						temp.append("PS");
				}
				ss = temp;
			}
			
			// check
			int pc = 0, rc = 0, sc = 0;
			for (int j = 0; j < (int)ss.size(); ++j)
			{
				if (ss[j] == 'P') pc++;
				else if (ss[j] == 'R') rc++;
				else sc++;
			}
			
			if (pc == p && rc == r && sc == s)
				res.push_back(ss);
		}

		if (res.size() <= 0)
		{
			out << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			for (int i = 0; i < res.size(); i++)
			{
				int kkk = res[i].size();
				for (int a = 2; a < kkk; a *= 2)
				{
					string temp = "";
					for (int j = 0; j < res[i].size(); j += (2*a))
					{
						string sa = res[i].substr(j, a);
						string sb = res[i].substr(j+a, a);
						if (sa.compare(sb) < 0)
						{
							temp.append(sa); temp.append(sb);
						}
						else
						{
							temp.append(sb); temp.append(sa);
						}
					}
					res[i] = temp;
				}


				/*for (int j = 0; j < res[i].size(); j += 2)
				{
					if (res[i][j] == 'R' && res[i][j+1] == 'P')
					{
						res[i][j] = 'P'; res[i][j+1] = 'R';
					}
					if (res[i][j] == 'S' && res[i][j+1] == 'R')
					{
						res[i][j] = 'R'; res[i][j+1] = 'S';
					}
					if (res[i][j] == 'S' && res[i][j+1] == 'P')
					{
						res[i][j] = 'P'; res[i][j+1] = 'S';
					}
				}
				for (int j = 0; j < res[i].size(); j += 4)
				{
					if (j + 4 > res[i].size())
						continue;
					string sub = res[i].substr(j, 4);
					if (sub == "PSPR")
					{
						res[i][j+1] = 'R'; res[i][j+3] = 'S';
					}
					else if (sub == "RSPS")
					{
						res[i][j] = 'P'; res[i][j+2] = 'R';
					}
					else if (sub == "RSPR")
					{
						res[i][j] = 'P'; res[i][j+1] = 'R'; res[i][j+2] = 'R'; res[i][j+3] = 'S';
					}
				}*/
			}

			sort(res.begin(), res.end());
			out << "Case #" << test << ": " << res[0] << endl;
		}
	}

	in.close();
	out.close();
	return 0;
}