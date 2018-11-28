/*
    This code has been written by MinakoKojima, feel free to ask me question. Blog: http://www.shuizilong.com/house
    Template Date: 2015.10.12
    Note: ...
*/


#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>

using namespace std;

#define	sqr(a)		((a)*(a))
#define	rep(i,a,b)	for(int i=(a);i<(int)(b);i++)
#define	per(i,a,b)	for(int i=((a)-1);i>=(int)(b);i--)
#define	PER(i,n)	per(i,n,0)
#define	REP(i,n)	rep(i,0,n)
#define	clr(a)		memset((a),0,sizeof (a))
#define	SZ(a)		((int)((a).size()))
#define	ALL(x)		x.begin(),x.end()
#define	mabs(a)		((a)>0?(a):(-(a)))
#define	inf			(0x7fffffff)
#define	eps			1e-6

#define	MAXN
#define MODN		(1000000007)

typedef long long ll;

#define TEST_LOCAL 1

char s[50001];

int main()
{
#if TEST_LOCAL
	freopen("in.txt","r",stdin);

	//freopen("out.txt","w",stdout);
#endif

	int T;
	scanf("%d",&T);

	rep(CASE,1,T + 1)
	{
		scanf("%s",s);
		int n = strlen(s);
		stack<char> st;
		int res = 0;
		REP(i,n)
		{
			if (st.empty() || st.top() != s[i])
			{
				st.push(s[i]);
			}
			else
			{
				st.pop();
				res += 10;
			}
		}
		res += st.size() / 2 * 5;

		printf("Case #%d: ",CASE);
		printf("%d\n",res);
	}

	return 0;
}
