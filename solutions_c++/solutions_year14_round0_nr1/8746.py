#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,A,B;
	cin>>t;
	for (int tt = 1; tt <= t; ++tt)
	{
		int i,j,k;
		int a[4][4];
		int b[4][4];
		int ct[17];
		int flag=0;
		int ans;
		int count=4;
		cin>>A;
		A--;
		for (int i = 0; i < 17; ++i)
		{
			/* code */
			ct[i]=0;
		}
		for (int i = 0; i < count; ++i)
		{
			/* code */
			for (int j = 0; j < count; ++j)
			{
				/* code */
				cin>>a[i][j];
				if (i==A)
				{
					/* code */
					ct[a[i][j]]++;
				}
			}
		}

		cin>>B;
		B--;
		for (int i = 0; i < count; ++i)
		{
			/* code */
			for (int j = 0; j < count; ++j)
			{
				/* code */
				cin>>b[i][j];
				if (i==B)
				{
					/* code */
					ct[b[i][j]]++;
				}
			}
		}
		for (int i = 1; i < 17; ++i)
		{
					if(ct[i]==2&&flag==1)
					{
						flag=2;//bad magician
						break;
					}
					if(ct[i]==2)
					{
						ans=i; //correct number
						flag=1;
					}
		}
		cout<<"Case #" << tt <<": ";
		if (flag==0)
		{
			cout<<"Volunteer cheated!\n";
		} else if (flag == 1)
		{
			cout<<ans<<endl;
		} else {
			cout<<"Bad magician!\n";
		}
	}

	return 0;
}