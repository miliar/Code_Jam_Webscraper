#include<stdio.h>
main()
{
	int t,i,a,b,k,j,p,x;
	FILE *ifp=fopen("test.in","r");
	FILE *ofp=fopen("result.txt","w");
	fscanf(ifp,"%d",&t);
	for(i=0;i<t;i++)
	{
	   fscanf(ifp,"%d",&a);	
	   fscanf(ifp,"%d",&b);
	   fscanf(ifp,"%d",&k);
		int count=0;
	   for(j=0;j<a;j++)
	   {
	   	  for(p=0;p<b;p++)
  	    {
  	    	x=j&p;  	    	
  	    	if(x<k)
  	    	count++;    	  	
    	  }
   		
        }
        fprintf(ofp,"Case #%d: %d\n",i+1,count);
	}
	fclose(ifp);
	fclose(ofp);
}