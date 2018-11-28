/*
Author : OmarEl-Mohandes
PROG   : C
LANG   : C++
*/
#include <map>
#include <string>
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
#include <vector>
#include <set>
#include <complex>
#include <memory.h>
using namespace std;

#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)m;i++)
#define REP(i,k,m) for(int i=k;i<(int)m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1061109567)
bool check(ll i)
{
	ss st;
	st << i;
	string tem;
	st >> tem;
	string r = tem;
	reverse(all(tem));
	return r == tem;
}
ll arr[]=
{
1 ,
4 ,
9 ,
121 ,
484 ,
10201 ,
12321 ,
14641 ,
40804 ,
44944 ,
1002001 ,
1234321 ,
4008004 ,
100020001 ,
102030201 ,
104060401 ,
121242121 ,
123454321 ,
125686521 ,
400080004 ,
404090404 ,
10000200001 ,
10221412201 ,
12102420121 ,
12345654321 ,
40000800004 ,
1000002000001 ,
1002003002001 ,
1004006004001 ,
1020304030201 ,
1022325232201 ,
1024348434201 ,
1210024200121 ,
1212225222121 ,
1214428244121 ,
1232346432321 ,
1234567654321 ,
4000008000004 ,
4004009004004
};
int main()
{
	freopen("C.in" , "rt" , stdin);
	freopen("C.out" , "wt" , stdout);
	int t ;
	ll a , b;
	cin >> t;
	rep(c , t)
	{
		cin >> a >> b;
		int cnt = 0;
		rep(i , 39)
			if(arr[i] >= a && arr[i] <= b)
				cnt ++;
		printf("Case #%d: %d\n" , c+1 , cnt);
	}
	return 0;
}

