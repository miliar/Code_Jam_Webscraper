#include<stdio.h>
 #include<stdlib.h>
  #include<algorithm>
   int main()
    { 
	int test,z=1;
	 scanf("%d",&test);
	  while(test--)
	   {
	    int n,i,c=0,l=0,j=0,k=0;
		 scanf("%d",&n); 
		 double arr[n],brr[n],a[n],b[n];
		  for(i=0;i<n;i++)
		   { 
		   scanf("%lf",&arr[i]);
		    }
			 for(i=0;i<n;i++) 
			 { 
			 scanf("%lf",&brr[i]);
			  } 
			  std::sort(arr,arr+n); 
			  std::sort(brr,brr+n);
			   for(i=0;i<n;i++)
			    {
				 a[n-1-i]=arr[i];
				  b[n-1-i]=brr[i];
				   } 
				   for(i=0;i<n;i++)
				    { 
					for(j=0;j<n;j++)
					 { 
					 if(brr[j]) 
					 {
					  if(brr[j]>arr[i])
					   {
					    brr[j]=0;
						 c++;
						  break;
						   }
						    }
							 }
							  }
							   c=n-c;
							    k=0;
								 l=0;
								  for(i=0;i<n;i++) 
								  { 
								  for(j=n-1;j>=0;j--)
								   {
								    if(b[j])
									 {
									  if(arr[i]>b[j])
									   { 
									   l++; b[j]=0;
									    arr[i]=0;
										 break; 
										 } 
										 else
										  { b[k++]=0;
										   arr[i]=0;
										    break;
											 }
											  }
											   }
											    }
												 printf("Case #%d: %d %d\n", z++,l,c);
												  }
												   return 0;
												    }

