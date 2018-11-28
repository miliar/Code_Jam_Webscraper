#include<iostream>
using namespace std;
int main()
{
	int a[4],b[4];
	int x,temp;
	int t,j,i,k;
	int count;
	cin>>t;
	for(i=0;i<t;i++)
	{
		count=0;
		cin>>x;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>temp;
				if(j==x-1)
				a[k]=temp;
			}
		}
		cin>>x;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>temp;
				if(j==x-1)
				b[k]=temp;
			}
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			if(a[j]==b[k])
			{
			count++;
			temp=a[j];
		    }
		}
		if(count==0)
		cout<<"Case #"<<(i+1)<<": Volunteer cheated!\n";
		else if(count==1)
		cout<<"Case #"<<(i+1)<<": "<<temp<<"\n";
		else
		cout<<"Case #"<<(i+1)<<": Bad magician!\n";
	}
	return 0;
}
