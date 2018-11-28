#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long t,x,n,num,temp,k,ar[11],i,res,r;
	FILE *ip,*op;
	ip=fopen("input.in","r");
	if(ip==NULL)
	{
		cout<<"ERROR!!";
		exit(0);
	}
	op=fopen("output.op","w");
	if(op==NULL)
	{
		cout<<"ERROR!!";
		exit(0);
	}
	fscanf(ip,"%lld",&t);
	k=1;
	while(t--)
	{   
	    for(i=0;i<=10;i++)
	      ar[i]=0;
	    fscanf(ip,"%lld",&n);
	   	x=10;temp=n;i=1,res=0;
	   	if(n==0)
	     fprintf(op,"Case #%lld: INSOMNIA\n",k);
	    else{
		 
			while(x>0)
			{
				num=temp*i;
				res=num;
				while(num!=0)
				{
					r=num%10;
					num=num/10;
					if(ar[r]==0)
					 {
					   ar[r]=22;
				        x--;
				     } 
				}
				i++;
			}
		fprintf(op,"Case #%lld: %lld\n",k,res);
		
	  }
	  k++;
	}
}
