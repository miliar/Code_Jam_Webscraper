#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int t;
	char file[]="A-large.in";
	FILE* f=fopen(file,"r");
	fscanf(f,"%d",&t);
	
	for(int i=0;i<t;i++)
	{
		int n;
		fscanf(f,"%d",&n);
		if(n==0)
		{
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			int h[10]={0},sum=0,ans,k=1,r;
		
			while(sum!=10)
			{
				r=k*n;
				ans=r;
				while(r)
				{
					int d=r%10;
					r=r/10;
					if(h[d]==0)
					{
						h[d]=1;
						sum++;
					}	
				}
				k++;	
			}
			cout<<"Case #"<<i+1<<": "<<ans<<endl; 
		}
		
	}
}
