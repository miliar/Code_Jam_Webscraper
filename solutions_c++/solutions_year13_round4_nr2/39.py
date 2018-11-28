#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define LL long long

using namespace std;

int tt;
int n;
LL p;

bool check1(LL x) { // guarantee
	LL les=x;
	LL posi=0;
	for (int i=0;i<n;++i) {
		posi<<=1;
		if (les>0) {
			posi++;
			les=(les-1)/2;
		}
	}
	if (posi<p) return true;
	else return false;
}

bool check2(LL x) { // can
	LL large=((LL)1 << (LL)n)-x-1;
	LL posi=0;
	for (int i=0;i<n;++i) {
		posi<<=1;
		if (large>0) {
			large=(large-1)/2;
		} else posi++;
	}
	if (posi<p) return true;
	else return false;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		cin >> n >> p;
		LL l=0,r=((LL)1 << (LL)n)-1;
		LL ans1=0;
		while (l<=r) {
			LL mid=(l+r)/2;
			if (check1(mid)) {
				ans1=mid;
				l=mid+1;
			} else r=mid-1;
		}
		LL ans2=0;
		l=0,r=((LL)1 << (LL)n)-1;
		while (l<=r) {
			LL mid=(l+r)/2;
			if (check2(mid)) {
				ans2=mid;
				l=mid+1;
			} else r=mid-1;
		}
		printf("Case #%d: ",ii);
		cout << ans1 << " " << ans2 << endl;
	}
}
