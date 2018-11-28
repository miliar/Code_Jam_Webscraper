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
template<class T>

T prime(T a , T b)
{
	cout << a << "\t"<<b << endl;
	if ( a >= b)
		return (prime(b , a));
	if(a == 0)
		return b;
	return prime(a , b%a);
}

string its(int n)
{
	string ret;
	if(n == 0)
	{
		ret = "0";
		return ret;
	}
	while(n > 0)
	{
		ret += (n % 10 + '0');
		n /= 10;
	}
	reverse(ret.begin() , ret.end());
	return ret;
}

int number(vector<string> &src , vector<int>& idxes)
{
	set<string> c;
	for(int i = 0 ; i < idxes.size() ; i++)
	{
		string t = src[idxes[i]];
		for (int l = 1 ; l <= t.size() ; l++)
			c.insert(t.substr(0 , l));
	}
	return c.size();
}

void getComb(vector <vector<vector <int> > >&comb , vector<vector<int> > idxs , int M , int N, int cur)
{
	if (cur == M)
	{
		for (int i = 0 ; i < N ; i++)
		{
			if (idxs[i].empty())
				return;
		}
		comb.push_back(idxs);
		return;
	}
	
	for (int i = 0 ; i < N ; i++)
	{
		idxs[i].push_back(cur);
		getComb(comb, idxs, M , N , cur + 1);
		idxs[i].pop_back();
	}
}

int main()
{
//==============in put=================
	ifstream curFile("D-small-attempt1.in");
	vector<int> result;
	vector<int> ways;
	int T; // testcases count
	int M;
	int N;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
//==============solution==================
			cout << "Enter Test case:" << c + 1 << endl;
			vector<string> src;
			curFile >> M;
			curFile >> N;
			for (int i = 0 ; i < M ; i++)
			{
				string t;
				curFile >> t;
				src.push_back(t);
			}
			vector< vector< vector<int> > > combine;
			vector< vector<int> > idxs(N, vector<int>());
			getComb(combine , idxs,  M ,N , 0);
//==============solution end==============
			int ret = 0;
			int siz = 0;
			for (int i = 0 ; i < combine.size() ; i++)
			{
				idxs = combine[i];
				int cur = 0;
				for(int j = 0 ; j < N ; j++)
				{
					cur += number(src , idxs[j]);
				}
				if (cur > ret)
				{
					ret = cur;
					siz = 1;
				}
				else if (cur == ret)
					siz ++;
			}
			result.push_back(ret + N);
			ways.push_back(siz);
		}	
	}
	curFile.close();
//==============out put==================
	ofstream outfile;
	outfile.open("result.txt");
	if(outfile.is_open())
	{
//		outFile << setprecision(6);
		for(int i = 0; i < result.size() ; i++) {
			outfile << "Case #" << i + 1<< ": " <<result[i] <<' '<<ways[i]<< endl;
			cout << "Case #" << i + 1<< ": " <<result[i]<<' '<<ways[i] << endl;
		}
	}
	outfile.close();
	return 0;
}
