#include <iostream>
#include <fstream>
using namespace std;

// void swap(int p[],int i,int j)
// {
// 	int t=p[i];
// 	p[i]=p[j];
// 	p[j]=t;
// }

// void paixu(int p[],int q[])
// {
// 	for (int i=0;i<3;i++)
// 	{
// 		for (int j=i;j<4;j++)
// 		{
// 			if (p[i]<p[j]) swap(p,i,j);
// 			if (q[i]<q[j]) swaq(q,i,j);
// 		}
// 	}
// }

void panduan(int p[], int q[],int id)
{
	// 	cout <<id<<": ";
	// for (int i = 0; i < 4; ++i)
	// {
	// 	cout <<p[i]<<' '<<q[i]<<endl;
	// }
	// paixu(p);
	// paixu(q);
	// int j=0;
	// for (int i=0;i<4;i++)
	// {
	// 	while (p[i]>q[j] && j<4) j++;
	// 	if (j==4) cout <<"Case #"<<id<<": "
	// 	if (p[i]<q[j]) continue;

	// }
	// int sum=0;
	int t=0;
	for (int i=0;i<4;i++)
	{
		for (int j=0;j<4;j++)
		{
			if (p[i]==q[j]) 
			{
				if (t==0)
				{
					t=p[i];
				}
				else 
				{
					cout << "Case #"<<id<<": Bad magician!"<<endl;
					return;
				}
			}
		}
	}
	// sum /=2;
	// if (sum==1)
	if (t==0)
	{
		cout << "Case #"<<id<<": Volunteer cheated!"<<endl;
		return;
	} 
	else 
	{
		cout << "Case #"<<id<<": "<<t<<endl;
		return;
	}
}

int main()
{
	freopen("magic.in","r",stdin);
	freopen("magic.out","w",stdout);
	int T;
	cin>>T;
	for(int id=1;id<T+1;id++)
	{
		int a1;
		cin >> a1;
		a1--;
		int p[10],q[10];
		int t[5][5];
		for (int i = 0; i < 10; ++i)
		{
			/* code */
			p[i]=0;
			q[i]=0;
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>t[i][j];
				if (a1==i)
				{
					p[j]=t[i][j];
				}
			}
		}
		int a2;
		cin>>a2;
		a2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>t[i][j];
				if (a2==i)
				{
					q[j]=t[i][j];
				}
			}
		}


		panduan(p,q,id);
	}
	return 0;
}