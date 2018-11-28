#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <map>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)

typedef long long LL;
const int maxn=120;
int bits[40];
map<int,vector<int> > M;

int chk(__int128 tmp) {
	for (LL i=2;i*i<=tmp;i++) {
		if (i>1000000) break;
		if (tmp%i==0) {
			return i;
		}
	}
	return 0;
}

int main() {
	//freopen("c.out","w",stdout);
	printf("Case #1:\n");
	bits[0]=1;
	bits[31]=1;
	int count=0;
	for (unsigned i=(1u<<31)+1u;i<=~0u;i+=2) {
		rep(k,2,10) {
			__int128 tmp=0,base=1;
			int t;
			rep(j,0,31) {
				tmp+=bits[j]*base;
				base*=k;
			}
			if ((t=chk(tmp))>0) {
				M[i].push_back(t);
			}
		}
		if (M[i].size()==9) {
			repd(j,31,0) printf("%d",bits[j]);
			rep(j,0,(int)M[i].size()-1)
				printf(" %d",M[i][j]);
			puts("");
			if (++count==500) break;
		}
		rep(k,0,1) {
			int j=0;
			while (!(bits[j]^=1)) j++;
		}
	}
	return 0;
}
