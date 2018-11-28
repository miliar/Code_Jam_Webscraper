/*************************************************************************

       Author:            palayutm
       Created Time :     Sat 28 May 2016 11:24:38 PM CST

       File Name:         d.cc
       Description:       new style, new life

 ************************************************************************/
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> PII;

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

int a[55][55];

bool check (int n){
//	FOR (i, 1, n){
//		FOR (j, 1, n){
//			cout << a[i][j] << " ";
//		}
//		cout << endl;
//	}
	bool flag = true;
	FOR (i, 1, n){
		vector<int> xx, yy;
		FOR (j, 1, n){
			if (j != i){
				xx.PB (j);
			}
			if (a[i][j] == 1){
				yy.PB(j);
			}
		}
		if (SIZE (yy) > SIZE (xx)){
			continue;
		}
		do{
			bool ff = true;
			FOR (i, 0, SIZE (yy)-1){
				if (a[xx[i]][yy[i]] == 0){
					ff = false;
				}
			}
			if (ff){
				flag = false;
				break;
			}
		}while(next_permutation(ALL(xx)));

	}
//	cout << flag << endl;
	return flag;
}

int main (){
	int T;
	cin >> T;
	FOR (cas, 1, T){
		vector<PII> vec;
		int n;
		cin >> n;
		FOR (i, 1, n){
			string s;
			cin >> s;
			FOR (j, 0, SIZE(s)-1){
				a[i][j+1] = (s[j] == '1');
				if (a[i][j+1] == 0){
					vec.PB (MP (i, j+1));
				}
			}
		}
		int ans = 10000000;
		if (SIZE (vec) == 0){
			ans = 0;
		}
		FOR (i, 0, (1<<SIZE(vec))-1){
			int cnt = 0;
			FOR (j, 0, SIZE (vec)-1){
				if ((1<<j)&i){
					a[vec[j].first][vec[j].second] = 1;
					cnt ++;
				}
			}	
		//	cout << cnt << endl;
			if (check (n)){
				ans = min(ans, cnt);
			}
			FOR (j, 0, SIZE (vec)-1){
				if ((1<<j)&i){
					a[vec[j].first][vec[j].second] = 0;
				}
			}	
		}
		printf ("Case #%d: %d\n", cas, ans);
	}
}

