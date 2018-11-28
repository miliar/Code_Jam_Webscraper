#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <queue>
#include <functional>
#include <stack>
#include <cstdlib>
#include <complex>
#include <sstream>
#include <memory.h>

typedef long long LL;

using namespace std;

string s;

int a[22];
int A[22];
int B[22];
int dpA[22];
int dpB[22];
bool ok = true;
bool broken = false;
int br = 0;
int d = 0;
int n;
int Count = 0;
bool used[22];
inline bool check()
{
	dpA[0] = 1;
	for ( int i = 1 ; i < n; i ++)
	{
		dpA[i] = 1;
		for ( int j = 0 ; j < i ; j ++)
		{
			if ( a[i] > a[j])
			{
				dpA[i] = max(dpA[i],dpA[j]+1);
			}
		}
		if ( dpA[i]!=A[i])
		{
			d = i;
			br = a[i];
			broken = true;
			return false;
		}
	}
	dpB[n-1] = 1;
	for ( int i = n-2; i >= 0; i --)
	{
		dpB[i] = 1;
		for ( int j = n-1; j > i; j --)
		{
			if ( a[j] <a[i])
			{
				dpB[i] = max(dpB[i],dpB[j] + 1);
			}
		}
		if ( dpB[i]!=B[i])
		{ 
			
			d = i;
			br = a[i];
			broken = true;
			return false;
		}
	}
	return true;
}
inline void ans()
{
	for ( int i = 0 ; i < n; i ++)
	{
		cout << a[i]<< ' ';
	}
}
inline void bust(int pos)
{
	if ( pos == n)
	{
		ok = check();
	}
	else if (!ok)
	{
		for ( int i = 1 ; i <= n; i ++)
		{
			
				if ( broken)
				{
					if ( a[d] != br)
						broken = false;
					if ( pos <= d)
						broken  = false;
				}
				else
				{
					if ( !used[i])
					{
			
					used[i] = true;
					a[pos] = i;
					bust(pos+1);
					used[i] = false;
						if ( ok) return;
						if ( broken)
						{
							if ( pos <= d)
						broken  = false;
						}
						
					}
				}
			

		}
	}
}
int main()
{
	//#ifndef _DEBUG
	    freopen("C-small-attempt2.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	//#endif
	int t;
	cin >> t;	
	for ( int k = 1 ; k <= t; k ++)
	{
		ok = false;
		cin >> n;
		for ( int i = 0 ; i <=n; i ++)
			used[i] = false;
		for ( int i = 0 ; i < n; i ++)
			cin >> A[i];
		for ( int  i =  0  ; i < n  ; i ++)
			cin >> B[i];
	    bust(0);
		printf("Case #%d: " , k);
		ans();
		cout << endl;
	}
	return 0;
}