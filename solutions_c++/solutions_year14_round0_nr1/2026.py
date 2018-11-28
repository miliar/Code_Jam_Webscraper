#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-small-attempt1.out","w",stdout);
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
		int n;
		int a[17];
		for (int i=1;i<17;i++) a[i] = 0;
		int r = 2;
		while(r--)
		{
			cin>>n;
			for (int i=0;i<4;i++)
				for (int j=0;j<4;j++)
				{
					int x;
					cin>>x;
					if (i==n-1)
						a[x] +=1;
				}
		}
		int ans = 0;
		int k;
		for (int i=1;i<17;i++)
			if (a[i] > 1)
			{
				ans += 1;
				k = i;
			}
		cout<<"Case #"<<tt<<": ";
		if (ans==0)
			cout<<"Volunteer cheated!\n";
			else if (ans == 1)
			cout<<k<<"\n";
			else cout<<"Bad magician!\n";
	}
	return 0;
}