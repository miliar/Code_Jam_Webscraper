/*************************************************************************

       Author:            palayutm
       Created Time :     Sat 09 Apr 2016 03:19:36 PM CST

       File Name:         a.cc
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

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

int main (){
	int T;
	cin >> T;
	FOR (cas, 1, T){
		string s;
		cin >> s;
		string t;
		t += s[0];
		FOR (i, 1, SIZE (s)-1){
			if (s[i] != s[i-1]){
				t += s[i];
			}
		}
		int ans = SIZE (t);
		if (t[ SIZE (t)-1 ] == '+'){
			ans --;
		}
		cout << "Case #" << cas << ": " << ans << endl;
	}
}

