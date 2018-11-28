#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
#include <queue>
#include <memory.h>

using namespace std;

long long getWorst(long long total,long long player) {
	long long ret=0,better=player;
	total>>=1;
	while(better>0) {
		ret+=total;
		better=(better-1)>>1;
		total>>=1;
	}
	return ret;
}

long long getBest(long long total,long long player) {
	long long ret=0,worst=total-1-player;
	total>>=1;
	while(total>0) {
		if (worst==0) ret+=total;
		else worst=(worst-1)>>1;
		total>>=1;
	}
	return ret;
}

void doTest() {
	long long n,p;
	cin >> n >> p;
//	for(int i=0;i<(1<<n);++i)
//		cout << i << "	" << getBest(1<<n,i) << "	" << getWorst(1<<n,i) << endl;
	long long l=0,r=(1LL<<n),total=1LL<<n;
	while(r-l>1) {
		long long m=(l+r)>>1;
		if (getWorst(total,m)<p) l=m;
		else r=m;
	}
	cout << l;
	l=0,r=(1LL<<n);
	while(r-l>1) {
		long long m=(l+r)>>1;
		if (getBest(total,m)<p) l=m;
		else r=m;
	}
	cout << " " << l;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test) {
		printf("Case #%d: ",test);
		doTest();
		printf("\n");
	}
	return 0;
}
