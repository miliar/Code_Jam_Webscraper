//Bismillahir Rahmanir Rahim
//#pragma warning(disable:4786)
//#pragma comment(linker,"/STACK:514850816")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <climits>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
using namespace std;

int main() {
	freopen("G://A-small-attempt0.in","r",stdin);
	freopen("G://A-small-attempt0.out","w",stdout);
	int t,i,a,b,c,d,ya,yb,yc,yd,za,zb,zc,zd, ans,cnt,r,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d",&r);
		for(j=1;j<=4;j++) {
			scanf("%d %d %d %d",&a, &b, &c, &d);
			if(j == r){
				ya = a, yb = b, yc = c, yd = d;
			}
		}
		scanf("%d",&r);
		for(j=1;j<=4;j++) {
			scanf("%d %d %d %d",&a, &b, &c, &d);
			if(j == r){
				za = a, zb = b, zc = c, zd = d;
			}
		}
		cnt = 0;ans = -1;
		if(ya == za || ya == zb || ya == zc || ya == zd){
			cnt++;
			ans = ya;
		}
		if(yb == za || yb == zb || yb == zc || yb == zd){
			cnt++;
			ans = yb;
		}
		if(yc == za || yc == zb || yc == zc || yc == zd){
			cnt++;
			ans = yc;
		}
		if(yd == za || yd == zb || yd == zc || yd == zd){
			cnt++;
			ans = yd;
		}
		printf("Case #%d: ",i);
		if(cnt == 0) printf("Volunteer cheated!");
		else if(cnt == 1) {
			printf("%d",ans);
		}
		else printf("Bad magician!");
		printf("\n");
	}
	return 0;
}