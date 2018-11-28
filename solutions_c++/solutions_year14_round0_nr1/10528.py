#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int kk;
	for(kk=1;kk<=t;kk++)
	{
		int *hit=new int [17];
		int row1,row2;
		cin>>row1;
		int i,j,k;
		for(k=1;k<=16;k++)
			hit[k]=0;
		
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				cin>>k;
				if(i==row1)
					hit[k]++;
			}
			
			cin>>row2;
		
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				cin>>k;
				if(i==row2)
					hit[k]++;
			}
			
			int count=0;
		for(i=1;i<=16;i++)
			if(hit[i]==2)
				count++;
			
			cout<<"Case #"<<kk<<": ";  
		if(count>=2)
			cout<<"Bad magician!\n";
		else if(count==0)
			cout<<"Volunteer cheated!\n";
		else
		{
			for(i=1;i<=16;i++)
				if(hit[i]==2)
					cout<<i<<"\n";
		}
	}
	return 0;
}