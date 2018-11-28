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

bool getD(int src , int pos)
{
	return src & (1 << pos);
}

LL getTail(int src , int pos)
{
	int ret = 1;
	while(pos > 0)
	{
		ret = ret << 1 + 1;
		pos --;
	}
	return ret & src;
}

LL getCount(int a , int b , int k , int d)
{
	if(d < 0)
		return 1;
	bool fa = getD(a , d);
	bool fb = getD(b , d);
	bool t = getD(k , d);
	if(fa && fb)
	{
		if(t)
		{
		}
		else
		{
			LL ret = 0;
			ret += getCount(a, b , k , d - 1);
			return ret;
		}
	}
	else if(fa)
	{
		if(t)
			return 0;
		//return getCount
		
	}
	else if(fb)
	{
		if(t)
			return 0;

	}
	else
	{
		if(t)
			return 0;

	}
}

int main()
{
//==============in put=================
	ifstream curFile("B-small-attempt1.in");
	vector<LL> result;
	int T; // testcases count
	int a;
 	int b;
	int k;
	LL A;
	LL B;
	LL ret;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
//==============solution==================
			curFile >> a;
			curFile >> b;
			curFile >> k;
			a -= 1;
			b -= 1;
			k -= 1;
/*
			if(a > b)
			{
				int t = a;
				a = b;
				b = a;
			}
			if(a <= k)
			{
				A = a + 1;
				B = b + 1;
				ret = A * B;
				result.push_back(ret);
				continue;
			}
			int d = 0;
			int t = b;
			while(t > 0)
			{
				d ++;
				t = t >> 1;
			}
			d -= 1;
*/
			ret = 0;
			for(int i = 0 ; i <= a ; i++)
				for(int j = 0 ; j <= b ; j++)
					ret += ( (i & j) <= k);
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
		for(int i = 0; i < result.size() ; i++)
			outfile << "Case #" << i + 1<< ": " <<result[i] << endl;
	}
	outfile.close();
	return 0;
}
