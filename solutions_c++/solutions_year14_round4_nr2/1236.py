/*
 * b.cpp
 *
 *  Created on: May 31, 2014
 *      Author: AhmedSamir
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <complex>

#ifdef _MSC_VER
#include<hash_set>
#include<hash_map>
using namespace stdext;
#else
#if __GNUC__ >2
#include<ext/hash_set>
#include<ext/hash_map>
using namespace __gnu_cxx;
#else
#include<hash_set>
#include<hash_map>
#endif
#endif

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#ifdef _MSC_VER
#define rep(i,m) for(decltype(m) i=0;i<m;i++)
#define repI(i,m) for(decltype(m.begin()) i = m.begin();i!=m.end();++i)
#define repRI(i,m) for(decltype(m.rbegin()) i = m.rbegin();i!=m.rend();++i)
#else
#define rep(i,m) for(__typeof(m) i=0;i<m;i++)
#define repI(i,m) for(__typeof(m.begin()) i = m.begin();i!=m.end();++i)
#define repRI(i,m) for(__typeof(m.rbegin()) i = m.rbegin();i!=m.rend();++i)
#endif
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define EPS (1e-9)
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;

#define SMALL_INPUT
//#define LARGE_INPUT


int arr[1010];
int cpy[1010];
int n;

inline bool test(int ind)
{

	for (int i = 1; i <= ind; ++i)
	{
		if (arr[cpy[i]] <= arr[cpy[i - 1]]) return false;
	}

	for (int i = ind + 1; i < n; ++i)
	{
		if (arr[cpy[i]] >= arr[cpy[i - 1]]) return false;
	}
//	cerr << endl;
//	for (int i = 0; i < n; ++i)
//		cerr << arr[cpy[i]] << " ";
//	cerr << endl;
	return true;
}
int tmp[1010];
inline int calc()
{
	int res = 0;
	for (int i = 0; i < n; ++i)
		tmp[i] = i;
	for (int i = 0; i < n; ++i)
	{
		int j = i;
		for (; j < n; ++j)
			if (tmp[j] == cpy[i]) break;
		for (; j > i; --j)
		{
			swap(tmp[j], tmp[j - 1]);
			res++;
		}
	}
//	for (int i = 0; i < n; ++i)
//		cerr << arr[tmp[i]] << " ";
//	cerr << endl;
	return res;
}

int main()
{
	freopen("b.in", "rt", stdin);
#ifdef SMALL_INPUT
	freopen("b-small-attempt2.in", "rt", stdin);
	freopen("b-small.2.txt", "wt", stdout);
#endif
#ifdef LARGE_INPUT
	freopen("b-large.in", "rt", stdin);
	freopen("b-large.txt", "wt", stdout);
#endif
	int tc;
	scanf("%d", &tc);
	rep(T,tc)
	{

		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", arr + i);
			cpy[i] = i;
		}

		//		memcpy(arr, cpy, n);
		//		sort(cpy, cpy + n);
		int mn = 1e9;
		do
		{
			bool f = 0;
			for (int i = 0; i < n; ++i)
			{
				if (test(i))
				{
					f = 1;
					break;
				}
			}
			if (f)
			{
				int x = calc();
//				for (int i = 0; i < n; ++i)
//					cerr << cpy[i] << " ";
//				cerr << " => " << x << endl;
				mn = min(mn, x);
			}
		} while (next_permutation(cpy, cpy + n));
		printf("Case #%d: %d\n", T + 1, mn);

#ifdef SMALL_INPUT
		cerr << T + 1 << " of " << tc << " is done." << endl;
#endif
#ifdef LARGE_INPUT
		cerr << T + 1 << " of " << tc << " is done." << endl;
#endif
	}
	return 0;
}
