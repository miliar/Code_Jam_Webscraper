#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int a,b,cases,n,i,j,count,k;
	
	scanf("%d",&cases);
	for(int t=1;t<=cases;t++)
	{
		count =0;
		cin>>a>>b>>k;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j) < k)
				{
					count ++;	
				}
				
			}	
			
		}	
		cout<<"Case #"<<t<<": "<<count<<endl;
		
		
		
	}

cin.get();
cin.get();
return 0;
}
