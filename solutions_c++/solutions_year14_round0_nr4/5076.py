#include <iostream>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>

#define gc() getchar()
int c;
#define read_int(n) n=0; c=gc();while(c<'0' || c>'9')c=gc();while(c>='0' && c<='9'){n= (n<<3)+(n<<1)+c-48;c=gc();}

using namespace std;

 int main() {

	int t,n,dec_war,kenscore;
	int i,j;
	float naomi[10];
	float ken[10];

	scanf("%d",&t);

	int k=1; //case_no

	while(k<=t)
	{    dec_war=0; kenscore=0;

		scanf("%d",&n);

		for(i=0;i<n;i++)
		{
		  scanf("%f",&naomi[i]);
        }

		for(i=0;i<n;i++)
		{
		  scanf("%f",&ken[i]);
        }

		  sort(naomi,naomi+n);
		  sort(ken,ken+n);

		  i=n-1;
		  j=n-1;

		  while((i>=0)&&(j>=0))
		    {
		    	if(naomi[i]>ken[j])
		    	   {
		    	   	dec_war++; //Naomi score
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
		      	 	kenscore++;
		      	 	i++;
		      	 	j++;
		      	 }
		      	else
		      	  {
		      	  	i++;
		      	  }
		      }


		  printf("Case #%d: %d %d\n",k,dec_war,n-kenscore);
		  k++;

	}
	return 0;
}
