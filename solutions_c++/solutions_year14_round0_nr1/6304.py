#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int count = 0;
		int val = -1;
		int a[4][4],b[4][4],ac,bc;
		cin>>ac;
		ac-=1;
		
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>a[j][k];
		
		cin>>bc;
		bc-=1;
		
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>b[j][k];
				
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if( a[ac][j] == b[bc][k] )
					count++,val=a[ac][j];
		
		cout<<"Case #"<<i<<": ";
		if(count==1)
			cout<<val<<"\n";
		else if(count==0)
			cout<<"Volunteer cheated!\n";
		else 
			cout<<"Bad magician!\n";
	}
	return 0;
}
