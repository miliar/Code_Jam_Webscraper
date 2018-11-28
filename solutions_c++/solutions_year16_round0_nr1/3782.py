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
//cout <<  __func__ << " : " << __LINE__ << endl;
typedef long long LL;
int t[10];
void cal(LL n)
{
	do {
		//cout <<  __func__ << " : " << __LINE__ << ": " << n%10 << endl;
		t[n%10] = 1;
		n = n/10;
	} while(n != 0);
}
int is_full()
{
	REP(i, 10)
		if(!t[i])
			return 0;
	return 1;
}

int main(void)
{
	int tc;
	LL nn, num;
	cin >> tc;
	REP(i, tc) {
		ZERO(t);
		cin >> num;
		FORE(ii, 1, 1<<10) {
			nn = num*ii;
			//cout <<  __func__ << " : " << __LINE__ << ": nn :  " << nn << endl;
			cal(nn);
			if(is_full()) {
				cout << "Case #" << i+1 << ": " << ii*num << endl;
				break;
			}
			else if (ii == (1<<10)) {
				cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
				break;
			}
		}
	}
	return 0;
}
