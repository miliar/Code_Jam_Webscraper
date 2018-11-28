#include<stdio.h>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

double P[1005],Q[1005];

int main()
{
int i,j,t,N,k,c,d,f,l,m;
scanf("%d",&t);

for(k=1;k<=t;k++)
{
	scanf("%d",&N);
	for(i=0;i<N;i++)
		scanf("%lf",&P[i]);
	
	for(i=0;i<N;i++)
		scanf("%lf",&Q[i]);
	

	sort(P,P+N);
	sort(Q,Q+N);
	//for(i=0;i<n;i++)printf("%.3f ",arr[i]);printf("\n");
	//for(i=0;i<n;i++)printf("%.3f ",Q[i]);printf("\n");
	c=d=0;
	j=0;	

	for(i=0;i<N;i++)
	{
		while(j<N&&P[j]<Q[i])j++;
		if(j<N)c++;
		else break;
		j++;
	}
    
	j=0;
	for(i=0;i<N;i++)
	{
		while(j<N&&P[i]>Q[j])j++;
		if(j<N)d++;
		else break;	
		j++;
	}
	printf("Case #%d: %d %d\n",k,c,N-d);
}
return 0;
}


