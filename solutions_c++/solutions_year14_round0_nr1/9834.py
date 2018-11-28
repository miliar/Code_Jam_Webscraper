#include<iostream>
using namespace std;

int main()
{
	int t,ans1,ans2,a[4][4],b[4][4],ans,k=0,x;

	cin>>t;

	while(t--)
	{
		ans=0;

		cin>>ans1;
		ans1--;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>a[i][j];

		cin>>ans2;
		ans2--;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>b[i][j];

		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(a[ans1][i]==b[ans2][j])
			{
				ans++;
				x=a[ans1][i];
			}
		}
		k++;

		if(ans==0)
		cout<<"Case #"<<k<<": Volunteer cheated!\n";

		if(ans==1)
		cout<<"Case #"<<k<<": "<<x<<"\n";

		if(ans>1)
		cout<<"Case #"<<k<<": Bad magician!\n";
	}
return 0;
}
