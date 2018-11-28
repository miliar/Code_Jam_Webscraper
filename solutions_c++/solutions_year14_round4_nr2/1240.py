#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main(void){
	int t,hh;
	scanf("%d",&t);
	for(hh=1;hh<=t;hh++){
		int n;
		scanf("%d",&n);
		int i,j;
		int s[15];
		int p[15];
		for(i=0;i<n;i++){
		  scanf("%d",&s[i]);
		  p[i]=s[i];
		}
		sort(s,s+n);
		int ans=10000000;
		do{
			int Max=0,a;
			for(i=0;i<n;i++){
				if(Max<s[i]) Max=s[i],a=i;
			}
			int ok=1;
			for(i=0;i<a;i++)
			  if(s[i]>s[i+1])
			    ok=0;
			for(i=a;i<n-1;i++)
			  if(s[i]<s[i+1])
			    ok=0;
			if(ok==1){
			/*	for(i=0;i<n;i++)
				  printf("%d ",s[i]);
				printf("\n");  */
				int d[15];
				for(i=0;i<n;i++)
				  for(j=0;j<n;j++)
				    if(s[i]==p[j])
				      d[i]=j;
			/*	for(i=0;i<n;i++)
				  printf("%d ",d[i]);
				printf("\n");    */
				int cc=0;
				for(i=0;i<n;i++)
				  for(j=i+1;j<n;j++)
				    if(d[i]>d[j])
				      cc++;
			//	printf("%d\n",cc);
				if(cc<ans) ans=cc;
			}
		} while(next_permutation(s,s+n));
	    printf("Case #%d: %d\n",hh,ans);
	}
	return 0;
}
