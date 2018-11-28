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

int up(vector<int>& src , int t)
{
	int head = 0;
	int tail = (int)src.size() - 1;
	while(head <= tail)
	{
		int mid = (head + tail) / 2;
		if (src[mid] < t)
			head = mid + 1;
		else
			tail = mid - 1;
	}
	return head;
}

int low(vector<int>& src , int t)
{
	int head = 0;
	int tail = (int)src.size() - 1;
	while(head <= tail)
	{
		int mid = (head + tail) / 2;
		if (src[mid] < t)
			head = mid + 1;
		else
			tail = mid - 1;
	}
	return tail;
}

int smallest(vector<int> & src)
{
	int ret = 0;
	int i = 0;
	int t = src[i];
	for ( ; i < src.size() ; i ++)
	{
		if (src[i] < t)
		{
			ret = i;
			t = src[i];
		}
	}
	return ret;
}

int main()
{
//==============in put=================
	ifstream curFile("B-large.in");
	vector<int> result;
	int T; // testcases count
	int N;
	vector<int> A;
	int t;
	int s;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
//==============solution==================
			cout << "Enter Test case:" << c + 1 << endl;
			curFile >> N;
			int ret = 0;
			A.clear();
			for (int i = 0 ; i < N ; i++)
			{
				curFile >> t;
				A.push_back(t);
			}
			while (A.size() > 1)
			{
				int id = smallest(A);
				ret += min(id , (int)A.size() - id - 1);
				A.erase(A.begin() + id);
			}
//==============solution end==============
			result.push_back(ret);
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

