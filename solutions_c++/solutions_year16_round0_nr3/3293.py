#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))
#define FOR(v,p,k) for(int v=p;v<k;++v)
#define FORE(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORC(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define ALL(c) c.begin(),c.end()
typedef long long LL;
//cout <<  __func__ << " : " << __LINE__ << endl;

LL powLL(int b, int p)
{
	LL ans = 1;
	REP(i, p)
		ans *= b;
	return ans;
}
LL cnv_2tob(LL b, LL n)
{
	LL ans = 0;
	LL bb = b;
	REP(i,14) {
		if (n&1) {
			ans += bb;
			n = n>>1;
		} else {
			n = n>>1;
		}
		bb *= b;
	}
	return ans;
}
void check(int b, LL i, LL d)
{
	LL ans;
	ans = powLL(b,15);
}
int main(void)
{
	int tc, N, J, cnt;
	LL n;
	LL div[11];
	cin >> tc;
	REP(i, tc) {
		cout << "Case #1:" << endl;
		cin >> N >> J;
		cnt = 0;
		REP(i, (2<<13)-1) {
			//cout <<  __func__ << " : " << __LINE__ << ": " << i << endl;
			ZERO(div);
			FORE(b,2,10) {
				n = powLL(b,15) + 1 + cnv_2tob(b,i);
				//cout <<  __func__ << " : " << __LINE__ << ": i b  n : " << i << " " << b << " " << n<< endl;
				//FOR(d, 2, n) {
				FOR(d, 2, min(n,(LL)100000)) {
					if(!(n%d)) {
						div[b] = d;
						check(b, i, d);
						break;
					}
				}
				if(!div[b])
					break;
			}
			if(div[10]) {
				cout << n << " ";
				FORE(i,2,10)
					cout << div[i] << " ";
				cout << endl;
				cnt++;
			//	cout << cnt << endl;
			}
			if(cnt == 50)
				break;
		}
	}
	return 0;
}
