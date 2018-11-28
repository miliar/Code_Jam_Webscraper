/*
* @Author: mkgaurab
* @FileName: B
* @Date:   2015-04-11 16:53:56
* @Last Modified by:   mkgaurab
* @Last Modified time: 2015-04-11 17:28:47
*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long Long;
typedef double DD;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef pair<int, int> PII;
typedef pair<Long, Long> PLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;

const int INF = 2000000000;
const int MOD = 1000000007;

#define sf scanf
#define pf printf
#define mem(a,b)          	memset(a,b,sizeof(a))
#define pb push_back
#define REP(i,a,b)        	for(int i=a; i<=b; ++i)
#define REPI(i,a,b,c)     	for(int i=a; i<=b; i+=c)
#define REPR(i,a,b)       	for(int i=b; i>=a; --i)
#define REPRD(i,a,b,c)    	for(int i=b; i>=a; i-=c)
#define REPB(i,a)         	for(int i=a; ;i++)
#define REPRB(i,a)        	for(int i=a; ; i--)
#define mp(a,b)   			make_pair(a,b)
#define fs        			first
#define sc        			second
#define SZ(s)     			((int)s.size())
#define PI        			3.141592653589793
#define VS        			vector<string>
#define VI        			vector<int>
#define VD        			vector<DD>
#define VL        			vector<Long>
#define VVL       			vector<VL >
#define lim       			1007
#define tlim      			(1<<((int)ceil(log2(lim))+1))
#define unq(vec)  			stable_sort(vec.begin(),vec.end());\
                  			vec.resize(distance(vec.begin(),unique(vec.begin(),vec.end())));
#define BE(a)     			a.begin(),a.end()
#define rev(a)    			reverse(BE(a))
#define sorta(a)  			stable_sort(BE(a))
#define sortc(a, comp)  	sort(BE(a),comp)

//int X[]={1,1,2,2,-1,-1,-2,-2},Y[]={2,-2,1,-1,2,-2,1,-1};//knight move
//int X[]={0,-1,-1,-1,0,1,1,1},Y[]={-1,-1,0,1,1,1,0,-1};//8 move
//int X[]={-1,0,1,0},Y[]={0,1,0,-1};//4 move
int A[lim], Res, lRes, tt, curr, maxavv;

int main(int argc, const char **argv)
{
	ios::sync_with_stdio(false);
	freopen("B_input_large.txt","r",stdin);
	freopen("B_output_large.txt","w",stdout);
	//double st=clock(),en;
	int Test, N;
	cin >> Test;
	REP(kase, 1, Test)
	{
		cin >> N;

		maxavv = -1;
		REP(i, 1, N) {cin >> A[i]; maxavv = max(maxavv, A[i]);}
		Res = maxavv;
		REP(i, 1, maxavv)
		{
			tt = lRes = 0;
			REP(j, 1, N)
			{
				if (A[j] > i)
				{
					lRes += (A[j] / i);
					if (A[j] % i == 0) lRes--;
					if (i > tt) tt = i;
				}
				else if (A[j] > tt) tt = A[j];
			}
			lRes += tt;
			Res = min(Res, lRes);
		}
		cout << "Case #" << kase << ": " << Res << endl;
	}
	//en=clock();
	//cerr<<(double)(en-st)/CLOCKS_PER_SEC<<endl;
	return 0;
}