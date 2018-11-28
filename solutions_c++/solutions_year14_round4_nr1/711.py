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


int main()
{
//==============in put=================
	ifstream curFile("A-large.in");
	vector<int> result;
	int T; // testcases count 
	int N;
	int X;
	int s;
	multiset<int> pool;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
//==============solution==================
			cout << "Enter Test case:" << c + 1 << endl;
			pool.clear();
			curFile >> N;
			curFile >> X;
			for (int i = 0 ; i < N ; i++)
			{
				curFile >> s;
				pool.insert(s);
			}
			int ret = 0;
			multiset<int> :: reverse_iterator rit;
			multiset<int> :: iterator it;
			while (!pool.empty())
			{
				rit = pool.rbegin();
				int t = * rit;
				it = pool.end();
				it --;
				pool.erase(it);
				ret ++;
				int m = X - t;
				it = pool.lower_bound(m);
				if (pool.empty())
					break;
				if (it == pool.end())
					it --;
				else if(*it > m)
				{	
					if (it == pool.begin())
						continue;
					it --;
				}
				pool.erase(it);
			}
			result.push_back(ret);
//==============solution end==============
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
			outfile << "Case #" << i + 1<< ": " <<result[i] << endl;
			cout << "Case #" << i + 1<< ": " <<result[i] << endl;
		}
	}
	outfile.close();
	return 0;
}
