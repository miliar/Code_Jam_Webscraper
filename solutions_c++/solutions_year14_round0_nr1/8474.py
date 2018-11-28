#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		int x,y;
		cin>>x;
		int array1[4];
		int array2[4];
		for(int j=1;j<=4;j++)
		{
			for(int k=0;k<=3;k++){
				int z;
				cin>>z;
				if(j==x)
				{
					array1[k]=z;
				}
			}	
		}
		cin>>y;
		for(int j=1;j<=4;j++)
		{
			for(int k=0;k<=3;k++){
				int z;
				cin>>z;
				if(j==y)
				{
					array2[k]=z;
				}
			}	
		}
		int count=0;
		int card;
		for(int k=0;k<=3;k++)
		{
			for(int l=0;l<=3;l++)
			{
				if(array1[k]==array2[l])
				{
					count++;
					card=array1[k];
				}
			}
		}
		if(count==0)
		{
			cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		}
		else if(count==1)
		{
			cout<<"Case #"<<i<<": "<<card<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
		}
	}		
}
