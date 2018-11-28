#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

main()
{
 	  int t,mat[4][4],user,user2, vet[4],vet2[4],i,j,k,cont1,cont2,cont3,cont4,p,x,tt,kk;
 	  scanf("%d",&t);
 	  tt=t;
 	  for(t;t>0;t--)
 	  {
       cont1=cont2=cont3=cont4=0;
       scanf("%d",&user);  
      for(i=0;i<4;i++)
 	  {
 	     for(j=0;j<4;j++)
 	     {
			 
  			 scanf("%d",&mat[i][j]);
			 if(i+1==user)	 
			 {
  			 vet[j]=mat[i][j];
			 }
			 
		 }
	  }
	  
	  scanf("%d",&user2);
	  
	  k=0;
	  p=0;
	  
	  for(i=0;i<4;i++)
 	  {
 	     for(j=0;j<4;j++)
 	     {
			 scanf("%d",&mat[i][j]);
		  
		  }
	  }
	  
	  for(i=0;i<4;i++)
 	  {
 	     for(j=0;j<4;j++)
 	     {
			 if(vet[p]==mat[i][j])
  			  {
					      if((user2-1)==i) kk=p;
						  p++;
		 				  vet2[k]=i; 
						  k++;
						  i=0;
						  j=-1;			    
						  
			  }
		  }
	  }
	  
	  x=0;
	  for(i=0;i<4;i++)
	  {
	    if(vet2[i]==(user2-1)) x++;
	  }
	  
	  printf("Case #%d: ",tt-t+1);
	  
	   	  if(x==0)
	   	  printf("Volunteer cheated!\n");
	   	  else if(x==1)
	   	  printf("%d\n",vet[kk]);
	   	  else
	   	  printf("Bad magician!\n");
	  
	  }
}
