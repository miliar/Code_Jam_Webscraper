#include<stdio.h>
 #include<stdlib.h>
  #include<algorithm>
   int main()
    { 
	int te,z=1,q;
	 scanf("%d",&te);
	 for(q=1;q<=te;q++)
	  
	   {
	    int n,i,kp=0,l=0,j=0,k=0;
		 scanf("%d",&n); 
		 double array[n],brray[n],a[n],b[n];
		  for(i=0;i<n;i++)
		   { 
		   scanf("%lf",&array[i]);
		    }
			 for(i=0;i<n;i++) 
			 { 
			 scanf("%lf",&brray[i]);
			  } 
			  std::sort(brray,brray+n); 
			  std::sort(array,array+n);
			   for(i=0;i<n;i++)
			    {
				 a[n-1-i]=array[i];
				  b[n-1-i]=brray[i];
				   } 
				   for(i=0;i<n;i++)
				    { 
					for(j=0;j<n;j++)
					 { 
					 if(brray[j]) 
					 {
					  if(brray[j]>array[i])
					   {
					    brray[j]=0;
						 kp++;
						  break;
						   }
						    }
							 }
							  }
							   kp=n-kp;
							    k=0;
								 l=0;
								  for(i=0;i<n;i++) 
								  { 
								  for(j=n-1;j>=0;j--)
								   {
								    if(b[j])
									 {
									  if(array[i]>b[j])
									   { 
									   l++; b[j]=0;
									    array[i]=0;
										 break; 
										 } 
										 else
										  { b[k++]=0;
										   array[i]=0;
										    break;
											 }
											  }
											   }
											    }
												 printf("Case #%d: %d %d\n", z++,l,kp);
												  }
												   return 0;
												    }
