#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <fstream>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion
// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("output.out");
	
	int n, sm, s[1003];
	char sr[1003];
	fin>>n;
	REP(i,1,n)
	{
		fin>>sm;
		fin>>sr;
		int l = strlen(sr), total = 0;
		REP(j,0,l-1)
		{
			s[j] = (int)(sr[j])-(int)('0');
			total += s[j];
		//	cout<<s[j]<<' ';
		}
		//cout<<endl;
		int stand = 0;
		REP(j, 0, l-1)
		{
			if (stand >= j )
				stand +=s[j];
		}
		if (stand==total)
		{
			fout<<"Case #"<<i<<": "<<0<<endl;
			continue;
		}
		
		stand = 0;
		int add = 0;
		REP(j, 0, l-1)
		{
			if (stand >= j)
				stand +=s[j];
			else if (stand < j)
			{
			//	cout<<j<<endl;
				add++;
				stand++;
				stand+=s[j];
			}
		}
		//cout<<' '<<endl;	
		fout<<"Case #"<<i<<": "<<add<<endl;
		
	}
	return 0;
}

