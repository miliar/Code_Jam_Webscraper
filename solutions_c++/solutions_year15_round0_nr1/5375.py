#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <queue>
#include <set>
#include <iostream>
#include <stack>
#include <list>
#include <iterator>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;

using namespace std;
vector<long long> A;
int main()
{
	ifstream in ("in.in");
	int t;
	in>>t;
	ofstream fout ("out.txt");
	for (int po=1; po<=t; ++po)
	{
		string s;
		int m;
		in>>m;
		in>>s;
		int kol=0;
		int fr=0;
		for (int i=0; i<s.length(); ++i)
		{
			int k=(int)s[i]-(int)'0';
			if (kol>=i)
				kol+=k;
			else
			{
				fr+=(i-kol);
				kol=i+k;
			}
		}
		fout<<"Case #"<<po<<": "<<fr<<endl;
	}	
	fout.close();
	in.close();
	return 0;
}