#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,x1=1;
	int k,n,l,a1,a2;
	double b;
	freopen("D-large.in","r",stdin);
	freopen("jame4.txt","w",stdout);
	scanf("%d",&t);
	while(t--) {
		a1=a2=0;
		scanf("%d",&n);
		double array1[n],array2[n],array3[n];
		for(k=0;k<n;k++) {
			scanf("%lf",&b);
			array1[k]=b;
		}
		for(k=0;k<n;k++) {
			scanf("%lf",&b);
			array2[k]=b;
			array3[k]=b;
		}
		sort(array1,array1+n);
		sort(array2,array2+n);
		sort(array3,array3+n);
		for(k=n-1;k>=0;k--) {
			for(l=n-1;l>=0;l--) {
				if(array1[k]>array2[l]&&array2[l]!=-1) {
					array2[l]=-1;
					a1++;
					break;
				}
			}
		}
		for(k=0;k<n;k++) {
			for(l=0;l<n;l++) {
				if(array3[k]>array1[l]&&array1[l]!=-1) {
					array1[l]=-1;
					a2++;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",x1++,a1,n-a2);
		
		
	}
	fclose(stdin);
fclose(stdout);
	
	return 0;
}
