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

int nums[256];

int main(){
	int T;
	cin >> T;
	
	rep(t,T){
		int A,leftnum;
		cin >> A;
		rep(i,A){
			int X; cin >> X;
			nums[i] = X;
			leftnum += X;
		}
		
		string ans;
		
		int cnts[256];
		rep(i,A){ cnts[i] = 0; }
		
		int cnt = 0;
		while( leftnum > 0 ){
			rep(i,A){
				if( nums[i] != 0 ){
					ans += 'A' + i;
					leftnum --;
					nums[i] --;
					cnt ++;
					if( leftnum == 0 ){ break; }
					if( cnt%2 == 0 ){ ans += " "; }
				}
			}
		}
		reverse(all(ans));
		printf("Case #%d: %s\n",t+1,ans.c_str());
	}
	return 0;
}
