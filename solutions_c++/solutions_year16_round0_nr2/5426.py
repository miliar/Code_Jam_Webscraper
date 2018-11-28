#include<iostream>
using namespace std;
int main()
{
	int i,t,j,count,lent,cases,cas;
	char a[105];
	cin>>cases;
	for(cas=1;cas<=cases;cas++)
	{
		cin>>a;	
		count = 0;
		lent = 0;
		for(j=0;a[j]!='\0';j++)
		{
			lent++;
		}
		if(lent!=1)
		{
			for(j=0;j<lent-1;j++)
			{	
				if(a[j]!=a[j+1])
				{
					count++;
				}
			}
		}
		if(a[lent-1]=='-')
		{
			count++;
		}
	    cout<<"Case #"<<cas<<": "<<count<<endl;
		
		
	}	
	return 0;
	
	
}
