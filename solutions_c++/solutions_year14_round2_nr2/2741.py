#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,i,a,b,k,l,j,res,ans,c;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d %d %d",&a,&b,&k);
		ans=0,res=0;
		for(j=1;j<a;j++){
			for(l=1;l<b;l++){
				res = 0;
				res = j&l;
				for(c=0;c<k;c++)
				{if(res==c)
				{ans++;break;}}
			}
		}
		ans = ans+a+b-1;
	
	
	
	printf("Case #%d: %d\n",i+1,ans);	
	}
	
return 0;
}

