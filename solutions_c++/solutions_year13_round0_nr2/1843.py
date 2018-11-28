/*
Author : OmarEl-Mohandes
PROG   : B
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
bool vis[101][101][2];
set<pair<pair<int , int> , int> > s;
int n , m;
int mat[101][101];
int dx[]={1,0};
int dy[]={0,1};
void computeS()
{
	s = set<pair<pair<int , int> , int> >();
	rep(i , n)
		rep(j , m)
			s.insert(mp(mp(mat[i][j] , j) , 0)) ,
			s.insert(mp(mp(mat[i][j] , i) , 1));
}
bool check(int num , int x , int y)
{
	if(y == 0){
		rep(i , n)
			if(mat[i][x] != num && mat[i][x] != 0)
				return 0;
	}
	else {
		rep(i , m)
			if(mat[x][i] != num && mat[x][i] != 0)
				return 0;
	}
	return 1;
}
int main()
{
	freopen("B.in" , "rt" , stdin);
	freopen("B.out" , "wt" , stdout);
	int t;
	scanf("%d" ,&t);
	rep(cas , t)
	{
		scanf("%d%d" ,&n , &m);
		memset(mat , 0 ,sizeof mat);
		rep(i , n)
			rep(j , m)
				scanf("%d" , &mat[i][j]);
		computeS();
		int num , x;
		bool y;
		for(__typeof (s.begin()) it = s.begin() ; it != s.end() ; it ++){
			num = it->first.first;
			x = it->first.second;
			y = it->second;
			if(check(num , x , y)){
				if(y == 0){
					rep(i , n)
						mat[i][x] = 0;
				}
				else
					memset(mat[x] , 0 , sizeof mat[x]);
			}
		}
		printf("Case #%d: " , cas+1);
		rep(i , n)
			rep(j , m)
				if(mat[i][j] != 0){
					printf("NO\n");
					goto exit;
				}
		printf("YES\n");
		exit:;
	}
	return 0;
}

