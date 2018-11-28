#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

double nao[1001],ken[1001];
bool nchk[10001],kchk[1001];

int main() {
	int test,z,x,y,i,j,n;
	int nao_min,nao_max,ken_min,ken_max;
	int check;

	freopen("D-large.in","r",stdin);
	freopen("d-large.txt","w",stdout);
	scanf("%d",&test);
	for ( z=1; z<=test; z++ ) {
		x=y=0;
		scanf("%d",&n);
		for ( i=0; i<n; i++ ) {scanf("%lf",&nao[i]);}
		for ( i=0; i<n; i++ ) {scanf("%lf",&ken[i]);}

		sort(nao,nao+n); sort(ken,ken+n);
		nao_min=0; ken_min=0;
		nao_max=n-1; ken_max=n-1;

		for ( i=0; i<n; i++ ) {nchk[i]=kchk[i]=true;} // init

		// x calculate
		for ( i=0; i<n; i++ ) {
			// ken[i];
			check=-1;
			for ( j=n-1; j>=0; j-- ) {
				if ( nchk[j] && nao[j]>ken[i] ) {
					check=j;
				}
				else break;
			}
			if ( check!=-1 ) {
				nchk[check]=false;
				x++;
			}
		}
		// y calculate
		for ( i=0; i<n; i++ ) {
			// nao[i];
			check=-1;
			for ( j=n-1; j>=0; j-- ) {
				if ( kchk[j] && ken[j]>nao[i] ) {
					check=j;
				}
				else break;
			}
			if ( check!=-1 ) {
				kchk[check]=false;
				y++;
			}
		}

		printf("Case #%d: %d %d\n",z,x,n-y);
	}
}