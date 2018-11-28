#include <bits/stdc++.h>
using namespace std;

int main()
{
     freopen ("D-small-attempt0.in","r",stdin); 
     freopen ("D-small-attempt0.out","w",stdout);
     // freopen ("input.in","r",stdin); 
     // freopen ("output.out","w",stdout);
     
     int i,j,n,t,k,c,s;
     scanf("%d",&t);
     for(int casenum=1; casenum<=t; casenum++){
     	scanf("%d %d %d",&k,&c,&s);
     	printf("Case #%d: ",casenum);
     	for(i=1;i<=k;i++)
     		printf("%d ",i);
     	printf("\n");
     }
	return 0;
}  