#include <iostream>
using namespace std;

int main() {
	int t,n,i,j,k,l,c[17],p,m,count,curr;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		count=0;curr=-1;
		for(j=0;j<17;j++)c[j]=0;
		cin>>p;
		for(j=1;j<=4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>m;
				if(j==p)
				{
					c[m]++;
				}
			}
		}
		cin>>p;
		for(j=1;j<=4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>m;
				if(j==p)
				{
					c[m]++;
				}
			}
		}
		for(j=1;j<17;j++)
		{
			if(c[j]==2)
			{
				count++;curr=j;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(count==0)
			cout<<"Volunteer cheated!";
		else if(count>1)
			cout<<"Bad magician!";
		else
			cout<<curr;
		cout<<endl;
	}
	// your code goes here
	return 0;
}
