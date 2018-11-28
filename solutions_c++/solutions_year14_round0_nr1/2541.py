#include <iostream>
using namespace std;
#include<map>

int main() 
{
	int t,x,i,j,a,count,k=0;
	cin>>t;
	int arr[4][4],brr[4][4];
	
	while(t--)
	{
		map<int,int> m;
	    map<int,int> ::iterator it;
		cin>>a;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>arr[i][j];
				if(i==a-1)
				{
					m[arr[i][j]]++;
				}
			}
		}
		count=0;
		cin>>a;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>brr[i][j];
				if(i==a-1)
				{
					it=m.find(brr[i][j]);
					if(it!=m.end())
					{
						count++;
						x=(*it).first;
						
					}
				}
			}
		}
		k++;
		if(count==1)
		{
			cout<<"Case #"<<k<<": "<<x<<endl;
		}
		else if(count==0)
		{
			cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		}
		else
			cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
	}

	return 0;
}