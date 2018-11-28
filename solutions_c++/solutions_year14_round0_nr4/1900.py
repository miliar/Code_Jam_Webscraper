#include<stdio.h>
#include<stdlib.h>
double a[1002],b[1002];

int fun(const void *a,const void *b)
{
   double pp=*(double*)a;
   double qq=*(double*)b;
   if(pp<qq)		return -1;
   else if(pp>qq)	return 1;
   else				return 0;
}

int main(){
	int t,z,n,i,j,ans;
	scanf("%d",&t);
	for(z=1;z<=t;z++){
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		qsort(a,n,sizeof(double),fun);
		qsort(b,n,sizeof(double),fun);
		j=0;
		ans=0;
		for(i=0;i<n;i++){
			while(j<n && (a[j]<b[i]))
				j++;
			if(j<n)	{ j++;ans++; }
			else	break;
		}
		printf("Case #%d: %d ",z,ans);
		j=0;
		ans=0;
		for(i=0;i<n;i++){
			while(j<n && (b[j]<a[i]))
				j++;
			if(j<n)	{ j++;ans++; }
			else	break;
		}
		printf("%d\n",n-ans);
	}
	return 0;
}





