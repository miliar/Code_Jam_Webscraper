//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}

int cnt[256];

int main(){
	int T;
	cin >> T;
	
	rep(t,T){
		rep(i,256){ cnt[i] = 0; }
		
		char str[2048];
		cin >> str;
		for(char *s=str;*s;s++){ cnt[(int)*s]++; }
		
		int numcnt[10];
		numcnt[0] = cnt[(int)'Z'];
		numcnt[2] = cnt[(int)'W'];
		numcnt[4] = cnt[(int)'U'];
		numcnt[6] = cnt[(int)'X'];
		numcnt[8] = cnt[(int)'G'];
		
		numcnt[3] = cnt[(int)'R'] - numcnt[4] -numcnt[0];
		numcnt[5] = cnt[(int)'F'] - numcnt[4];
		numcnt[7] = cnt[(int)'S'] - numcnt[6];
		numcnt[9] = cnt[(int)'I'] - numcnt[5] - numcnt[6] -  numcnt[8];
		numcnt[1] = cnt[(int)'O'] - numcnt[0] - numcnt[2] -  numcnt[4];
		
		//rep(i,10){ printf("%d:%d\n",i,numcnt[i]); }
		
		string ans = "";
		rep(i,10){
			rep(j,numcnt[i]){ ans += ('0' + i); }
		}
		
		
		printf("Case #%d: %s\n",t+1,ans.c_str());
	}
	return 0;
}
