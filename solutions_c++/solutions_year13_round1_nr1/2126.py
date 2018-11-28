#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	for(int it=0;it<n;it++)
	{
		int r,t,jum;
		scanf("%d %d",&r,&t);
		int dlm = r*r;
		int luar = (r+1)*(r+1);
		jum = luar-dlm;
		int tot = 0;
		int bil = jum;
		do{
			bil+=4;
		//	printf("%d ",bil);
			jum = jum+bil;
			tot+=1;
		}while(jum<=t);
		printf("Case #%d: %d\n",it+1,tot);

	}
	return 0;
}
