#ifdef __GNUC__
#include <ext/hash_map>
#include <ext/hash_set>
#else
#include <hash_map>
#include <hash_set>
#endif

namespace std
{
 using namespace __gnu_cxx;
}

#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <algorithm>
#include <math.h>
#include <cstdlib>
#include <climits>
#include <iomanip> 
using namespace std;

typedef long long LL;
typedef long double LD;

int main()
{
//==============in put=================
	ifstream curFile("A-small-attempt1.in");
	vector<string> result;
	int T; // testcases count
	int N;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
//==============solution==================
			curFile >> N;
			string pat;
			vector<vector <int> > count;
			string cur;
			string cpat;
			vector<int> ccount;
			string ret;
			for(int i = 0 ; i < N ; i++)
			{
                cpat.clear();
                ccount.clear();
				curFile >> cur;
				char a = cur[0];
				int t = 1;
            	int j = 1;
				while(j < cur.size())
                {
                    if(cur[j] == a)
					{
						t += 1;
					}
					else
					{
						cpat += a;
						ccount.push_back(t);
						a = cur[j];
						t = 1;
					}
					j++;
                }
				cpat += a;
				ccount.push_back(t);
				if(pat.empty())
				{	
					count.push_back(ccount);
					pat = cpat;
				}
				else if(pat == cpat)
					count.push_back(ccount);
				else
				{
					ret = "Fegla Won";
					break;
				}
			}	
			if(!ret.empty())
			{
				result.push_back(ret);
				continue;
			}
			int r = 0;
			for(int i = 0 ; i < count[0].size(); i++)
			{
				vector<int> curp;
				for(int j = 0 ; j < N ; j ++)
				{
					curp.push_back(count[j][i]);
				}
				sort(curp.begin(), curp.end());
				int mid = (N -1) / 2;
				int t = curp[mid];
				for(int j = 0 ; j < N ; j ++)
				{
					r += abs(curp[j] - t);
				}
			}
			if(r == 0)
				ret = "0";
			else
			{
				while(r > 0)
				{
					ret += (r % 10 + '0');
					r /= 10;
				}
				reverse(ret.begin() , ret.end());
			}
			result.push_back(ret);
//==============solution end==============
		}	
	}
	curFile.close();
//==============out put==================
	ofstream outfile;
	outfile.open("resultA.txt");
	if(outfile.is_open())
	{
//		outFile << setprecision(6);
		for(int i = 0; i < result.size() ; i++)
			outfile << "Case #" << i + 1<< ": " <<result[i] << endl;
	}
	outfile.close();
	return 0;
}
