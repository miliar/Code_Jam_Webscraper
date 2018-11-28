#include<iostream>
int main()
{
	int j,k,N,i,A[100],flag,ch,in,count1,jm,t;
	long long val,ans,ans1[13],l;
		freopen("3rd.in","r",stdin);
		freopen("output3rd.txt","w",stdout);
	scanf("%d",&t);
	
	scanf("%d",&N);
	scanf("%d",&jm);
	 	A[0]=1;
	  A[N-1]=1;	 
	  count1=0;
	  printf("Case #1:\n");
	for(int i = 0;i < (1 << (N-2)); ++i)
    {
     // printf("coing insiede\n");
        for(int j = 0;j < (N-2);++j)
        {
		
            if(i & (1 << j))
            {
				A[j+1]=1;
			}
            else
            {
			
             	A[j+1]=0;
	    	 }
	    
		}
		flag=0;
		for(in=0;in<11;in++)
		{
			ans1[in]=0;
		}
		for(k=2;k<=10;k++)
		{
			val=1;ans=0;
			  for(int m=0;m<N;m++)
			  {
					ans=ans+A[m]*val;
					val=val*k;		  	   
			  }
		//	  printf("%lld is ans %d \n",ans,k);
		//	  printf("%d is N\n",N);
			  for(l=2;(l*l)<=ans;l++)
			  {
			  //	printf("chaecdc\n");
			  	if(ans%l==0)
			  	{
			        ans1[k]=l;
			  		break;
				  }
			  }
	// printf("%lld is l\n",l);
			  
			
		} 
		for(ch=2;ch<=10;ch++)
			  {
			  	if(ans1[ch]==0)
			  	{
			  		
			  		flag=1;
				  }
			  }
			  if(flag==0)
			  {
			  	count1++;
			  	//printf("going inside\n");
			  	 for(int k=N-1;k>=0;k--)
	   			 {
	    		 	printf("%d",A[k]);
				 }
				 printf(" ");
			  		for(ch=2;ch<=10;ch++)
			  {
			  	    printf("%lld ",ans1[ch]);
			  }
			  if(count1>=jm)
			  {
			  	break;
			  }  
			  printf("\n");
				}	  
		
	
	//	 printf(" %d is i %d os n\n",i,N);
}
fclose(stdin);
	fclose(stdout);
	return 0;
}
