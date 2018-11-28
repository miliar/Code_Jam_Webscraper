//#define NDEBUG

#include <iostream>
#include <fstream>
#include <bitset>
#include <vector>
#include <queue>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <sstream>
#include <string>
#include <numeric>

using namespace std;

#define all(c) c.begin(),c.end()
#define nl '\n'
#define printv(v) for (long long i=0 ; i<v.size() ; i++) cout<<v[i]<<" "; cout<<nl;
#define printpv(v) for (long long i=0 ; i<v.size() ; i++) cout<<v[i].first<<","<<v[i].second<<" "; cout<<nl;
#define maxnum 50005
#define inf 1000000000

ifstream fin ("cj2.in");
ofstream fout ("cj2.out");

int t;

bool ispal(int x)
{
	stringstream ss;
	ss<<x;
	string xs=ss.str();

	vector<char> aha;
	for (int i=0 ; i<xs.length() ; i++) aha.push_back(xs[i]);

	reverse(all(aha));

	for (int i=0 ; i<aha.size() ; i++)
		if (aha[i]!=xs[i]) return false;
	return true;
}

int main()
{
	fin>>t;

	vector<int> palsquares;
	for (int i=0 ; i<=26 ; i++)
		if (ispal(i) && ispal(i*i)) palsquares.push_back(i*i);

	printv(palsquares);

	for (int m=0 ; m<t ; m++)
	{
		long long a, b;
		fin>>a>>b;
		int c=0;
		for (int i=0 ; i<palsquares.size() ; i++)
		{
			if (palsquares[i]<a) continue;
			if (palsquares[i]>b) break;
			c++;
		}
		fout<<"Case #"<<m+1<<": "<<c<<nl;
	}

}

