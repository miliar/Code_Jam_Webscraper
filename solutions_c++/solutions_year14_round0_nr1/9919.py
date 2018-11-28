#include <iostream>
using namespace std;

int main() {
	int x,t,r1,r2,a[4][4],b[4][4],ans,count;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		count=0;
		cin>>r1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>r2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		r1--;
		r2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[r1][i]==b[r2][j])
				{ans=a[r1][i];count++;}
			}
		}
		if(count==1)
		cout<<"Case #"<<x<<": "<<ans<<endl;
		else if(count>1)
		cout<<"Case #"<<x<<": Bad magician!"<<endl;
		else
		cout<<"Case #"<<x<<": Volunteer cheated!"<<endl;
	}
	return 0;
}