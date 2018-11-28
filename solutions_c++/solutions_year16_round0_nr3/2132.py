#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int t,c;
	cin>>t;

		long long int n, p, i;
		cin>>n;
		cin>>p;
		cout<<"Case #1:"<<endl;
		if (n==16)
		{
			for (i=0;i<50;i++)
			{
				int a[6];
				int j;
				for (j=0;j<6;j++)
					a[j]=0;

				int iCopy = i;
				int k=0;
				while(iCopy!=0)
				{
					a[k]=iCopy%2;
					iCopy=iCopy/2;
					k++;
				}

				cout<<"1";
				for (k=0;k<6;k++)
					cout<<a[k];
				cout<<"11";
				for (k=0;k<6;k++)
					cout<<a[k];
				cout<<"1 ";

				int power[11];
				for (j=2;j<=10;j++)
				{
					power[j]=pow(j,8)+1;
				}

				for (j=2;j<=10;j++)
				{
					if (j%2==0)
					{
						cout<<power[j]<<" ";
					}
					else
					{
						cout<<"2 ";
					}
				}
				cout<<endl;



			}
		}
		else if (n==32)
		{
			for (i=0;i<500;i++)
			{
				long long int a[14];
				long long int j;
				for (j=0;j<14;j++)
					a[j]=0;

				long long int iCopy = i;
				long long int k=0;
				while(iCopy!=0)
				{
					a[k]=iCopy%2;
					iCopy=iCopy/2;
					k++;
				}

				cout<<"1";
				for (k=0;k<14;k++)
					cout<<a[k];
				cout<<"11";
				for (k=0;k<14;k++)
					cout<<a[k];
				cout<<"1 ";

				long long int power[11];
				for (j=2;j<=10;j++)
				{
					power[j]=1;

					for (k=0;k<16;k++)
						power[j]=power[j]*j;
					power[j]=power[j]+1;
				}

				for (j=2;j<=10;j++)
				{
					if (j%2==0)
					{
						cout<<power[j]<<" ";
					}
					else
					{
						cout<<"2 ";
					}
				}
				cout<<endl;



			}
		}

	return 0;
}