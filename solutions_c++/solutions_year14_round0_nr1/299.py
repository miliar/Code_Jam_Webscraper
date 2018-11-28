#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;

int n,m,i,j,k,ttt,tt,r,a[10][10],f[20],y;
long long ans;

int main(){
	File;
	SC(ttt);
	n=4;
	for (tt=1; tt<=ttt; tt++){
		SC(r);
		for (i=0; i<=16; i++)
			f[i]=0;
		for (i=1; i<=n; i++)
			for (j=1; j<=n; j++){
				SC(a[i][j]);
				if (i==r) f[a[i][j]]=1;
			}
		SC(r);
		y=0;
		for (i=1; i<=n; i++)
			for (j=1; j<=n; j++){
				SC(a[i][j]);
				if (i==r && f[a[i][j]]){
					if (y==0) y=a[i][j];
					else y=17;
				}
			}
		printf("Case #%d: ",tt);
		if (y==17) printf("Bad magician!\n");
		else if (y==0) printf("Volunteer cheated!\n");
		else printf("%d\n",y);
	}
	return 0;
}
