#include<iostream>
#include<omp.h>
using namespace std;

long long calculate(int a,int b,int k,int count)
{
	
		for(long long i=0;i<a;i++)
		{
			for(long long j=0;j<b;j++)
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
				long long count=0;
				cin>>a>>b>>k;
				count=calculate(a,b,k,count);
				cout<<"Case #"<<x<<":"<<" "<<count<<"\n";
				
			}
}
