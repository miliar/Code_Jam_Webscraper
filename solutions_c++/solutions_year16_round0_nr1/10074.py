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
#define tin freopen("aain.txt","r",stdin)
#define tout freopen("aaout.txt","a",stdout)

void inp() {
#ifndef ONLINE_JUDGE
    freopen("aain.txt","r",stdin);
#endif
}

const int INF = 0x7fffffff;


int main()
{
	//tin;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","a",stdout);
	int t, i, k, dv;
	long long tmp, n, mul, ans;
	bool fl[10];

	S(t);

	ans = 0;

	F(i, 1, t + 1) {
		SL(n);


		F(k, 0, 10) {
			fl[k] = false;
		}

		
		k = 0;

		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}

		mul = 1;

		while (true) {

			tmp = n * mul;

			while (tmp > 0) {
				dv = tmp % 10;

				if (!fl[dv]) {
					fl[dv] = true;
					k++;
				}

				tmp /= 10;
			}

			if (k == 10) {
				ans = n * mul;
				break;
			}

			mul++;

		}


		printf("Case #%d: %lld\n", i, ans);



	}


	return 0;
}




