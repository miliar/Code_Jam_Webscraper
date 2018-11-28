#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int v=0;
	int a[4][4],temp;
	int y=0;
	while(t--)
	{
		int n;
		cin>>n;
		n--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		int m,temp2,ans=0;
		bool f=false,g=false;
		int b[4][4];
		cin>>m;
		m--;
		int x=0,count=-1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
				temp2=b[i][j];
				if(i==m)
				{
					for(int k=0;k<4;k++)	
					{
						if(temp2==a[n][k])
						{	
							ans=temp2;
							count++;
						}
					}
				}
			}
		}
		cout<<"CASE #"<<(v+1)<<": ";
		if(count==0)
		{
			cout<<ans<<endl;
		}
		else if(count>0)
		{
			cout<<"Bad magician!"<<endl;
		}
		else
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		v++;
	}
	return 0;
}