// Author: Kamil Nizinski
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <math.h>
#include <cstring>
#include <vector>
#define debug(fmt,...) fprintf(stderr,fmt, ## __VA_ARGS__)

using namespace std;
int wyst[17];
void solve() {
	int i,j,nr,x,q,w,szuk;
	for(i=1;i<=16;i++) wyst[i]=0;
	for(q=1;q<=2;q++) {
		scanf("%d",&nr);
		for(i=1;i<=4;i++) if(i==nr) {
			for(j=1;j<=4;j++) {
				scanf("%d",&x);
				wyst[x]++;
			}
		}
		else {
			for(j=1;j<=4;j++) scanf("%d",&x);
		}
	}
	w=0;
	szuk=0;
	//for(x=1;x<=16;x++) debug("wyst[%d]: %d\n",x,wyst[x]);
	for(x=1;x<=16;x++) if(wyst[x]==2) {
		szuk=x;
		w++;
	}
	if(w==1) {
		printf("%d\n",szuk);
		return;
	}
	if(w==0) {
		printf("Volunteer cheated!\n");
		return;
	}
	if(w>1) {
		printf("Bad magician!\n");
		return;
	}
}
int main() {
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++) {
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}