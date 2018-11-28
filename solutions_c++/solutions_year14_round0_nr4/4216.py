#include<bits/stdc++.h>
using namespace std;

/*int partition(double a[], int p, int r) 
{
	int j, i, s;
	j = p-1;
	for(i = p; i < r; i++) {
		if(a[i] <= a[r]) {
			j++;
			s = a[j];
			a[j] = a[i];
			a[i] = s;
		}
	}
	s = a[r];
	a[r] = a[j+1];
	a[j+1] = s;
	return j+1;
}
void qsort(double a[], int p, int r)
{
	int q;
	if(p < r) {
		q = partition(a, p, r);
		
		qsort(a, p, q-1);
		qsort(a, q+1, r);
	}
}*/

int main()
{
	int t, x=1;
	freopen("D-large.in","r",stdin);
	freopen("cc4.txt","w",stdout);
	scanf("%d", &t);
	while(t--) {
	int i, j, k, n, l, an1=0, an2=0, c1=0, c2=0;
		scanf("%d", &n);
		double a1[n];
		double a2[n];
		double a3[n];
		for(i=0;i<n;i++) {
			scanf("%lf",&a1[i]);
		}
		for(j=0;j<n;j++) {
			scanf("%lf",&a2[j]);
			a3[j]=a2[j];
		}
//		qsort(a1,1,n);
	//	qsort(a2,1,n);
	//	qsort(a3,1,n);
		sort(a1,a1+n);
		sort(a2,a2+n);
		sort(a3,a3+n);
		for(i=n-1;i>=0;i--) {
			if(a2[i] == 1)
			c1++;
			for(j=n-1;j>=0;j--) {
				if(a1[i]>a2[j]) {
					if(a2[j]!= -1) {
					
					a2[j]=-1;
					an1++;
					break;
				}
			}
			}
		}
		for(i=0;i<n;i++) {
			if(a1[i]==-1)
			c2++;
			for(j=0;j<n;j++) {
				if(a3[i]>a1[j]) {
					if(a1[j]!= -1){
					
					a1[j]=-1;
					an2++;
					break;
				}
				}
			}
		}
		printf("Case #%d: %d %d\n",x++,an1,n-an2);
		
		
	}
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
