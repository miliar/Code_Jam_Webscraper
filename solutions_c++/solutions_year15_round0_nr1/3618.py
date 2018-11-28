/* Aniket Kumar */
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
#include <cmath>
#include <unistd.h>
#include <algorithm>
#include <vector>
#include <map>
#include <climits>
#include <set>

using namespace std;

#define V(a) vector<a>
#define pi pair<int,int>
#define ull unsigned long long
#define ill long long
#define F(i,a,n) for(i=(a);i<(n);++i)
#define RP(i,n) F(i,0,n)
#define SUM(v, s, i) RP(i, v.size()){ s += v[i];}
#define MP(a, b) make_pair(a, b)
#define fs first
#define se second
#define S(x) scanf("%d",&x)
#define SL(x) scanf("%lld",&x)
#define SZ(x) (x.size())
#define PB(a) push_back(a)
#define dbug(i,size,x) F(i,0,size){cout<<x[i]<<" ";} cout<<endl

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i, j, t, sm, cs, cur;

	int pstd, pnd;

	char ch[1002];

	S(t);

	F(cs, 1, t + 1) {
		scanf("%d %s", &sm, ch);

		pstd = 0;
		pnd = 0;

		F(i, 0, sm + 1) {

			cur = ch[i] - '0';

			if (pstd < i && cur > 0) {

				pnd += (i - pstd);
				pstd = i;
			}			

			pstd += cur;
		}

		printf("Case #%d: %d\n", cs, pnd);
	}

	return 0;
}

