#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	
		int i,j,k,l,n,t1,a[10000],c[100],t,flag,pos,max1,pos2=-1,count1;
			freopen("A.in","r",stdin);
		freopen("output1th.txt","w",stdout);
		scanf("%d",&t);
		flag=0;
	 for(t1=1;t1<=t;t1++)
	    {
	    
	    	flag=0;
	    	scanf("%d",&n);
	    	for(i=0;i<30;i++)
	    	{
	    		c[i]=0;
			}
	    	for(i=0;i<n;i++)
	    	{
	    		scanf("%d",&a[i]);
				c[i]=a[i];
			}
				printf("Case #%d: ",t1);
			while(flag!=1)
			{
			pos2=-1;
			max1=0;
			count1=0;
	    	for(i=0;i<26;i++)
	    	{
	    	   if(c[i]>max1)
	    	   {
	    	   	max1=c[i];
				pos=i;	
					if(max1==1)
			   	{
			   		
			   		count1++;
				   }
			   }
			   else if(c[i]==max1)
			   {
			   	pos2=i;
			   	if(max1==1)
			   	{
			   		
			   		count1++;
				   }
			   }
			   
			}	
		 //    printf("%d is count1\n",count1);
			if(max1==0)
			{
				flag=1;
				break;
			}
			else if(pos2!=-1&&c[pos2]==max1&&max1!=1||pos2!=-1&&c[pos2]==max1&&count1==2||pos2!=-1&&c[pos2]==max1&&count1>3)
			{
				c[pos]--;
				c[pos2]--;
				printf("%c%c ",pos+'A',pos2+'A');
			}
			else
			{
					c[pos]--;
		
				printf("%c ",pos+'A');
			}
	    }
	    printf("\n");
		}
//	
	fclose(stdin);
	fclose(stdout);
	

	
	return 0;
}
