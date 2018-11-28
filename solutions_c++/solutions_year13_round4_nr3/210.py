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

int a[2002],b[2002];
int tmp[22];
bool dp[1<<20];

int bc(int mask) {
	int ret=0;
	while(mask) {
		ret+=mask&1;
		mask>>=1;
	}
	return ret;
}

int getL(int n,int mask,int cnt) {
	int ret=0;
	for(int i=0;i<cnt;++i) {
		if (mask&(1<<i)) ret=max(ret,a[i]);
	}
	return ret;
}

int getR(int n,int mask,int cnt) {
	int ret=0;
	for(int i=0;i<cnt;++i)
		if (mask&(1<<(n-1-i))) ret=max(ret,b[n-1-i]);
	return ret;
}

bool ok(int n,int filled) {
	int umask=0;
	for(int i=0;i<filled;++i) {
		umask|=(1<<tmp[i]);
	}
	memset(dp,0,sizeof(dp));
	dp[0]=1;
	int total=1<<n;
	for(int i=0;i<n;++i) {
		if (umask&(1<<i)) {
			for(int pos=0;pos<filled;++pos) {
				if (tmp[pos]==i) {
					for(int mask=0;mask<total;++mask) {
						if (dp[mask]&&bc(mask)==i&&(mask&(1<<pos))==0) {
							if (getL(n,mask,pos)==a[pos]-1&&getR(n,mask,n-1-pos)==b[pos]-1)
								dp[mask|(1<<pos)]=true;
						}
					}
				}
			}
			continue;
		}
		for(int mask=0;mask<total;++mask) {
			if (dp[mask]&&bc(mask)==i) {
				for(int pos=0;pos<n;++pos) {
					if ((mask&(1<<pos))==0) {
						if (getL(n,mask,pos)==a[pos]-1&&getR(n,mask,n-1-pos)==b[pos]-1)
							dp[mask|(1<<pos)]=true;
					}
				}
			}
		}
	}
	return dp[total-1];
}

void doTest() {
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
		scanf("%d",&a[i]);
	for(int i=0;i<n;++i)
		scanf("%d",&b[i]);
	bool used[22]={0};
	int ans[22]={0};
	for(int pos=0;pos<n;++pos) {
		for(int nx=0;nx<n;++nx) {
			if (!used[nx]) {
				tmp[pos]=nx;
				if (ok(n,pos+1)) {
					ans[pos]=nx;
					used[nx]=true;
					break;
				}
			}
		}
	}
	for(int i=0;i<n;++i)
		cout << " " << ans[i]+1;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test) {
		printf("Case #%d:",test);
		doTest();
		printf("\n");
	}
	return 0;
}
