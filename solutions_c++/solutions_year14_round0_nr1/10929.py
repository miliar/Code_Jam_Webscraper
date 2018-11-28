#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	// your code goes here
	int n,i,num,j,k,a[4],ans,b[4],dumb,nans;
	scanf ("%d",&n);
	for (i=0;i<n;i++){
		nans=0;
		scanf ("%d",&num);
		for (j=0;j<num-1;j++) scanf ("%d %d %d %d",&dumb,&dumb,&dumb,&dumb);
		scanf ("%d %d %d %d",&a[0],&a[1],&a[2],&a[3]);
		for (j=0;j<4-num;j++) scanf ("%d %d %d %d",&dumb,&dumb,&dumb,&dumb);
		//printf ("%d %d %d %d\n",a[0],a[1],a[2],a[3]);
		scanf ("%d",&num);
		for (j=0;j<num-1;j++) scanf ("%d %d %d %d",&dumb,&dumb,&dumb,&dumb);
		scanf ("%d %d %d %d",&b[0],&b[1],&b[2],&b[3]);
		for (j=0;j<4-num;j++) scanf ("%d %d %d %d",&dumb,&dumb,&dumb,&dumb);
		for (j=0;j<4;j++)for (k=0;k<4;k++)if (a[j]==b[k]){
			ans=b[k];
			nans++;
		}
		printf ("Case #%d: ",i+1);
		if (nans==0)printf ("Volunteer cheated!\n");
		if (nans>1) printf ("Bad magician!\n");
		if (nans==1) printf ("%d\n",ans);
	}
	return 0;
}