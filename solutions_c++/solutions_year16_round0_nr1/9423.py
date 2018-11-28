#include<bits/stdc++.h>
using namespace std;

int main()
{
	FILE *in;
	FILE *out;
	in=fopen("abcde.in","r");
	out=fopen("c.in","w");
	long long int t,c,n;
	
	
	fscanf(in,"%lld",&t);
	
	c=1;
	while(c<=t)
	{
		fscanf(in,"%lld",&n);
		long long int org=n;
		int visited[10];
		int  k,count=-1,d;
		long long int temp;
			
		long long int ans,j=2;
		
		for(k=0;k<10;k++)
			visited[k]=0;
			
		if(n==0)
			fprintf(out,"Case #%lld: INSOMNIA\n",c);
			
		else
		{
				
			while(1)
			{
				
				temp=n;
			
				while(n!=0)
				{
					d=n%10;
					n=n/10;
					if(visited[d]==0)
					{
						count++;
						visited[d]=1;
					}
				
					if(count==9)
					{
						
						ans=temp;
						break;
						
					}
				}
				if(count==9)
					break;
				n=org*j;
				j++;
				
			}
			fprintf(out,"Case #%lld: %lld\n",c,ans);
			

		}
		c++;
				
	
	}
	fclose(in);
	fclose(out);
	return 0;
}
