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

int n,m,i,j,k,ttt,tt,t,a[500][500];
long long ans;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		SC(n);SC(m);SC(k);
		printf("Case #%d:\n",tt);
		if (n*m-k==1){
			for (i=1; i<=n; i++){
				for (j=1; j<=m; j++){
					if (i==n && j==m) printf("c");
					else printf("*");
				}
				printf("\n");
			}
			continue;
		}
		if (min(n,m)==1){
			if (n*m-2<k) printf("Impossible\n");
			else {
				if (n==1) {
					for (j=1; j<=k; j++)
						printf("*");
					for (j=k+1; j<=m-1; j++)
						printf(".");
					printf("c\n");
				} else {
					for (j=1; j<=k; j++)
						printf("*\n");
					for (j=k+1; j<=n-1; j++)
						printf(".\n");
					printf("c\n");
				}
			}
			continue;
		}
		if (min(n,m)==2) {
			if (k&1 || n*m-k<4) {printf("Impossible\n"); continue;}
			if (n==2){
				for (i=1; i<=2; i++){
					for (j=1; j<=k/2; j++)
						printf("*");
					for (j=k/2+1; j<m; j++)
						printf(".");
					if (i==1) printf(".\n");
					else printf("c\n");
				}
			} else {
				for (j=1; j<=k/2; j++)
					printf("**\n");
				for (j=k/2+1; j<n; j++)
					printf("..\n");
				printf(".c\n");
			}
			continue;
		}
		t=n*m-k;
		//if (t==7 || t==5 || t==3 || t==2) {printf("Impossible\n"); continue;}
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
				a[i][j]=0;
		for (i=1; i<=n-2 && k; i++)
			for (j=1; j<=m-2 && k; j++){
				if (i!=n-2 || j!=m-2){
					a[i][j]=1;
					--k;
				}
			}
		for (i=1; i<=n-3 && k>1; i++){
			a[i][m]=1;
			a[i][m-1]=1;
			k-=2;
		}
		for (j=1; j<=m-3 && k>1; j++){
			a[n][j]=1;
			a[n-1][j]=1;
			k-=2;
		}
		if (k==1) a[n-2][m-2]=1;
		else if (k==3){
			a[n-2][m-2]=1;
			a[n-2][m-1]=1;
			a[n-2][m]=1;
		}
		else if (k==5){
			a[n-2][m-2]=1;
			a[n-2][m-1]=1;
			a[n-2][m]=1;
			a[n-1][m-2]=1;
			a[n][m-2]=1;
		}
		else if (k==0);
		else {printf("Impossible\n"); continue;}
		for (i=1; i<=n; i++){
			for (j=1; j<=m; j++)
				if (i==n && j==m) printf("c");
				else printf("%c",a[i][j] ? '*' : '.');
			printf("\n");
		}
	}
	return 0;
}
