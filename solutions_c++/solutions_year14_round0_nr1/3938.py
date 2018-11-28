#include<iostream>

using namespace std;

int main()
{
	int hash[17],r,t,arr[4][4];
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		for(int i=1;i<17;i++)
			hash[i]=0;
		cin>>r;
		r--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr[i][j];
		for(int i=0;i<4;i++)
			hash[arr[r][i]]++;
		cin>>r;
		r--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				cin>>arr[i][j];
		}
		for(int i=0;i<4;i++)
			hash[arr[r][i]]++;
		int c=0;
		for(int i=1;i<17;i++)
		{
			if(hash[i]==2)
				c++;
		}
		if(c==0)
			cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		else if(c==1)
		{
			for(int i=0;i<17;i++)
			if(hash[i]==2)
			cout<<"Case #"<<k<<": "<<i<<endl;
		}
		else
			cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
	}	
}