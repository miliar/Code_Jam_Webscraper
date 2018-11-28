#include <stdio.h>
#include<iostream>
#include <algorithm>
using namespace std;
double node[1002],pen[1002],a[1002],b[1002];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,n,j,k;
	int x,sum;
	cin>>t;
	for(i=0;i<t;i++) {
		x = 0;
		sum=0;
		cin>>n;
		for(j=0;j<n;j++) {
			cin>>node[j];
			a[j] = node[j];
		}
		for(j=0;j<n;j++) {
			cin>>pen[j];
			b[j] = pen[j];
		}
		sort(node,node+n);
		sort(pen,pen+n);
		sort(a,a+n);
		sort(b,b+n);
		for(j=0;j<n;j++) {
			for(k=0;k<n;k++) {
				if(node[k] > pen[j]) {
					node[k] = 0;
					pen[j] = 0;
					x++;
					break;
				}
			}
		}
		for(j=0;j<n;j++) {
			for(k=0;k<n;k++) {
				if(b[k] > a[j]) {
					sum++;	b[k] = 0;
					a[j] = 0;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i+1,x,n-sum);
	}
	return 0;
}
