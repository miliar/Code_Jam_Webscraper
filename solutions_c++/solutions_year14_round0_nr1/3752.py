#include <iostream>
using namespace std;

int main()
{
	int c1[6][6], c2[6][6];
	int t, r1, r2, i, j, k, m, ans;
	cin>>t;
	for(i=1; i<=t; i++)
	{
		cin>>r1;
		for(j=1; j<5; j++)
		{
			for(k=1; k<5; k++) cin>>c1[j][k];
		}
		cin>>r2;
		for(j=1; j<5; j++)
		{
			for(k=1; k<5; k++) cin>>c2[j][k];
		}
		m=0;
		for(j=1; j<5; j++)
		{
			for(k=1; k<5; k++)
			{
				if(c1[r1][j]==c2[r2][k])
				{
					m++;
					ans=c1[r1][j];
				}
			}
		}
		cout<<"Case #"<<i<<": ";
		if(m==0) cout<<"Volunteer cheated!";
		else if(m==1) cout<<ans;
		else cout<<"Bad magician!";
		cout<<endl;
	}

	return 0;
}
