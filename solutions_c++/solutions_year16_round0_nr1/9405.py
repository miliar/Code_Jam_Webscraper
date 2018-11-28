#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,j=1;
	FILE *f1,*f2;
	f1=fopen("A-large.in","r");
	f2=fopen("a.in","w");
	fscanf(f1,"%d",&t);
	while(t--)
	{
		
		int v[11];
		for(int i=0;i<11;i++)
			v[i]=0;
		long long int n,temp,org;
		fscanf(f1,"%lld",&n);
		org=n;
		if(n==0)
		fprintf(f2,"Case #%d: INSOMNIA\n",j);
		  else{
		int count=0,i=2;
		while(1)
		{
			temp=n;
			while(n)
			{
				int t=n%10;
				if(!v[t])
				{
					v[t]=1;
					count++;
				}
				n=n/10;
				if(count==10)
				{
					break;
				}
			}
			if(count==10)
			{
				break;
			}
			n=org*i;
			i++;
			
		}
		fprintf(f2,"Case #%d: %lld\n",j,temp);
		}
		j++;
	
	}
		fclose(f1);
		fclose(f2);
	return 0;
}
