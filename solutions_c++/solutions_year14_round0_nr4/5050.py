
#include <iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;


 int main() {
	int t,n,dw,w;
	int i,j;
	float naomi[10];
	float ken[10];
	scanf("%d",&t);
	int temp=t;
	while(t--)
	{    dw=0; w=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{

		  scanf("%f",&naomi[i]);}
		for(i=0;i<n;i++)
		{

		  scanf("%f",&ken[i]);}

		  sort(naomi,naomi+n);
		  sort(ken,ken+n);
		  i=n-1;
		  j=n-1;

		  while((i>=0)&&(j>=0))
		    {
		    	if(naomi[i]>ken[j])
		    	   {
		    	   	dw++;
		    	   	i--;
		    	   	j--;
		    	   }
		    	else
		    	 {
		    	 	j--;
		    	 }
                     }
		    i=0;j=0;
		    while((i<n)&&(j<n))
		      {
		      	if(ken[i]>naomi[j])
		      	 {
		      	 	w++;
		      	 	i++;
		      	 	j++;
		      	 }
		      	else
		      	  {
		      	  	i++;
		      	  }
		      }


		  printf("Case #%d: %d %d\n",temp-t,dw,n-w);

	}
	return 0;
}
