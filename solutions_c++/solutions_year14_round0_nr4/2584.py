#include <stdio.h>
#include<iostream>
#include <algorithm>
using namespace std;
double naomi[1002],ken[1002],a[1002],b[1002];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,n,j,k;
	int x,z;
	cin>>t;
	for(i=0;i<t;i++) {
		x = 0;
		z = 0;
		cin>>n;
		for(j=0;j<n;j++) {
			scanf("%lf", &naomi[j]);
			a[j] = naomi[j];
		}
		for(j=0;j<n;j++) {
			scanf("%lf", &ken[j]);
			b[j] = ken[j];
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		sort(a,a+n);
		sort(b,b+n);

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
					z++;
					b[k] = 0;
					a[j] = 0;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i+1,x,n-z);
	}
	return 0;
}
