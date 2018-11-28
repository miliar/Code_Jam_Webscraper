#include<iostream>
using namespace std;

int card1[4],card2[4];

int main()
{
	int t,n,aux;
	cin>>t;
	for(int k = 0;k < t;k++)
	{
		cin>>n;
		cout<<"Case #"<<k+1<<": ";
		for(int i = 0;i < 4;i++)
			for(int j = 0;j < 4;j++)
			{
				if(i==n-1)
					cin>>card1[j];
				else
					cin>>aux;
				
			}
		cin>>n;
		for(int i = 0;i < 4;i++)
			for(int j = 0;j < 4;j++)
			{
				if(i==n-1)
					cin>>card2[j];
				else
					cin>>aux;
				
			}
		int cont=0;
		int pos;
		for(int i = 0;i < 4; i++)
			for(int j = 0;j < 4; j++)
			{
				if(card1[i]==card2[j])
				{
					pos=i;
					cont++;
				}	
			}
		if(!cont)
			cout<<"Volunteer cheated!"<<endl;
		else if (cont==1)
			cout<<card1[pos]<<endl;
		else
			cout<<"Bad magician!"<<endl;
			
	}
	return 0;

}
