#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>

#define Inf 2147483647
#define Pi acos(-1.0)
#define N 1000000
#define LL long long

inline LL Power(int b, int p) { LL ret = 1; for ( int i = 1; i <= p; i++ ) ret *= b; return ret; }
const int dr [] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dc [] = {0, 1, 1, 1, 0, -1, -1, -1};

#define F(i, a) for( int i = (0); i < (a); i++ )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(i, x) for(typeof (x.begin()) i = x.begin(); i != x.end (); i++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Max(a, b)  (a < b ? b : a)
#define Min(a, b)  (a > b ? b : a)

using namespace std;

int main(int argc, const char ** argv) 
{
	int t;
	int table1[4][4];
	int table2[4][4];
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		int a1, a2;
		cin>>a1;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				int temp;
				cin>>temp;
				table1[j][k]=temp;
			}
		}
		cin>>a2;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				int temp;
				cin>>temp;
				table2[j][k]=temp;
			}
		}
		int table3[17];

		// for (int j = 0; j < 4; ++j)
		// {
		// 	cout<<table1[a1-1][j]<<'\t';
		// }
		// 	cout<<endl;
		// for (int j = 0; j < 4; ++j)
		// {
		// 	cout<<table2[a2-1][j]<<'\t';
		// }
		// 	cout<<endl;

		// index problem
		for (int j = 0; j < 17; ++j)
		{
			table3[j]=0;
		}
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				// printf("%d %d\n", table1[a1-1][j], table2[a2-1][k]);
				if (table1[a1-1][j] == table2[a2-1][k]) table3[table1[a1-1][j]]++;
			}
		}
		int found = 0;
		int number = 0;
		// index problem
		for (int j = 0; j < 17; ++j)
		{
			if (table3[j] > 0)
			{
				found++;
				number = j;
			}
		}
		if (found == 1)
		{
			printf("Case #%d: %d\n", i+1, number);
		}
		if (found >= 2)
		{
			printf("Case #%d: Bad magician!\n", i+1);
		}
		if (found == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", i+1);
		}
	}
	    
    return 0;	
}