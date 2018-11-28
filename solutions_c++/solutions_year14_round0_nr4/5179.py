// Author: Kamil Nizinski
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <math.h>
#include <cstring>
#include <vector>
#include <algorithm>
#define debug(fmt,...) fprintf(stderr,fmt, ## __VA_ARGS__)
#define mp make_pair
#define ft first
#define sd second
using namespace std;
typedef double dd;
int n;
vector < dd > A,B;
vector < pair < dd , bool > > W;
void solve() {
	int i,j,odp=0,S=0,maks=0,pA,qA,pB,qB;
	dd x;
	scanf("%d",&n);
	A.clear();
	B.clear();
	W.clear();
	for(i=1;i<=n;i++) {
		scanf("%lf",&x);
		B.push_back(x);
		W.push_back(mp(x,0));
	}
	for(i=1;i<=n;i++) {
		scanf("%lf",&x);
		A.push_back(x);
		W.push_back(mp(x,1));
	}
	sort(A.begin(),A.end());
	sort(B.begin(),B.end());
	sort(W.begin(),W.end());
	/*for(i=0;i<2*n;i++) debug("%d ",W[i].sd);
	debug("\n");*/
	
	pA=0;
	qA=n-1;
	
	for(i=0;i<n;i++) {
		if(B[i]>A[pA]) {
			pA++;
			odp++;
		}
		else {
			qA--;
		}
	}
	
	for(i=0;i<2*n;i++) {
		if(W[i].sd==1) S++;
		else S--;
		maks=max(maks,S);
	}
	printf("%d %d\n",odp,maks);
	/*i=n-1;
	j=0;
	while(i>=0 && A[i]>B[j]) {
		i--;
		j++;
	}
	printf("%d ",i+1);
	while(i>=0 && A[i]>B[0]) i--;
	printf("%d\n",i+1);*/
}
int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) {
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}