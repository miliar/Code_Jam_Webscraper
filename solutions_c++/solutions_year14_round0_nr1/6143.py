
/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

/*******  All Required define Pre-Processors and typedef Constants *******/
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",&t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (typeof(l.begin()) it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define mp make_pair
#define pb push_back
#define INF = (int)1e9;
#define EPS = 1e-9;
#define PI = 3.1415926535897932384626433832795;
#define MOD 1000000007
#define read(type) readInt<type>()
const double pi=acos(-1.0);
typedef pair<int, int> II;
typedef vector<int> VI;
typedef vector<II> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SET;
typedef multiset<int> MSET;
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;

/****** Template of Fast I/O Methods *********/
template <typename T> inline void write(T x)
{
	int i = 20;
	char buf[21];
	// buf[10] = 0;
	buf[20] = '\n';

	do
	{
		buf[--i] = x % 10 + '0';
		x/= 10;
	}while(x);
	do
	{
		putchar(buf[i]);
	} while (buf[i++] != '\n');
}

template <typename T> inline T readInt()
{
	T n=0,s=1;
	char p=getchar();
	if(p=='-')
		s=-1;
	while((p<'0'||p>'9')&&p!=EOF&&p!='-')
		p=getchar();
	if(p=='-')
		s=-1,p=getchar();
	while(p>='0'&&p<='9') {
		n = (n<< 3) + (n<< 1) + (p - '0');
		p=getchar();
	}

	return n*s;
}
/********** Main()  function *******/
int main()
{

	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int tc,row,card;
	tc = read(int);

	REP(k,tc){
        MPII mp;
        row = read(int);
        REP(i,4){
            REP(j,4){
                card = read(int);
                if(i==row-1)
                    ++mp[card];
            }
        }
        row = read(int);
        REP(i,4){
            REP(j,4){
                card = read(int);
                if(i==row-1 && mp.count(card)>0 )
                    ++mp[card];
            }
        }

        /**  check for unique ans **/
        int cnt1 = 0,cnt2 = 0,cd=0;
        FOREACH(it,mp){
            if(it->second==2){
                ++cnt2;
                cd = it->first;
            }
            if(it->second==1){
                ++cnt1;
            }
        }
        if(cnt2==1 && cnt1==3){
            printf("Case #%d: %d\n",k+1,cd);
        }else if(cnt1==4){
            printf("Case #%d: Volunteer cheated!\n",k+1);
        }else{
            printf("Case #%d: Bad magician!\n",k+1);
        }

	}
	return 0;
}
