#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string.h>
#include<vector>
#include<cmath>
#include<limits.h>
#define MOD 1000000009
#define MAX 1005

using namespace std;

double naomi[1002],ken[1002],a[1002],b[1002];
int main()
{
	int test,i,n,j,k;
	int x,count;
	scanf("%d",&test);
	for(i=0;i<test;i++) {
		x = 0;
		count=0;
		cin>>n;
		for(j=0;j<n;j++) {
			cin>>naomi[j];
			a[j] = naomi[j];
		}
		for(j=0;j<n;j++) {
			cin>>ken[j];
			b[j] = ken[j];
		}

		sort(ken,ken+n);
		sort(naomi,naomi+n);
		sort(b,b+n);
		sort(a,a+n);

		for(j=0;j<n;j++) {
			for(k=0;k<n;k++) {
				if(naomi[k] > ken[j]) {
					naomi[k] = 0;
					ken[j] = 0;
					x++;
					break;
				}
			}
		}
		for(j=0;j<n;j++) {
			for(k=0;k<n;k++) {
				if(b[k] > a[j]) {
					count++;
					b[k] = 0;
					a[j] = 0;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i+1,x,n-count);
	}
	return 0;
}
