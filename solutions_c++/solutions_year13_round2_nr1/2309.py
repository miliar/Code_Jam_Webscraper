/*
Author : OmarEl-Mohandes
PROG   : A
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
int main()
{
	freopen("test.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int t;
	scanf("%d" , &t);
	rep(c , t)
	{
		int st , n;
		scanf("%d%d" , &st , &n);
		vi v(n);
		rep(i , n)
			scanf("%d" , &v[i]);
		sort(all(v));
		int j = 0;
		int steps = 0;
		while(j < n){
			if(st > v[j])
				st += v[j] , j ++;
			else if(st-1 > 0){
				int k = 0;
				while(st <= v[j])
					st += (st-1) , k ++;
				st += v[j];
				if(k+steps >= (n-j) + steps)
				{
					steps += n-j;
					break;
				}
				else{
					steps += k;
				}
				j ++;
			}
			else{
				steps += n-j;
				break;
			}
		}
		printf("Case #%d: %d\n" , c+1 , steps);
	}
	return 0;
}

