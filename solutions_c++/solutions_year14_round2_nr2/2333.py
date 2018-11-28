#include<iostream>
#include<omp.h>
using namespace std;

long cal(int a,int b,int k,int count)
{
	
		for(long i=0;i<a;i++)
		{
			for(long j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					count++;
				}
			}
		}
	return count;			
}
int main()
{
		int tes,a,b,k,x=1;
		cin>>tes;
		
			for(x=1;x<=tes;x++)
			{
				long count=0;
				cin>>a>>b>>k;
				count=cal(a,b,k,count);
				cout<<"Case #"<<x<<":"<<" "<<count<<"\n";
				
			}
}
