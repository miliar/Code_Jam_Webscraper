#include<iostream>

using namespace std;

int main()
{
	int t,fa,sa,i,j,k=0,ans;
	cin>>t;
	while(t--)
	{
		k++;
		cin>>fa;
		fa--;
		int inarr[4][4];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>inarr[i][j];
			}
		}
		cin>>sa;
		sa--;
		int searr[4][4];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{	
				cin>>searr[i][j];
			}
		}
		
		int c=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				c+=(inarr[fa][i]==searr[sa][j]);
				if(inarr[fa][i]==searr[sa][j])
					ans=inarr[fa][i];
			}
		}
		if(c==1)
		{
			cout<<"Case #"<<k<<": "<<ans<<endl;
		}
		else if (c==0)
		{
			cout<<"Case #"<<k<<": Volunteer cheated!\n";
		}
		else
		{	
			cout<<"Case #"<<k<<": Bad magician!\n";
		}
	}
	return 0;
}
