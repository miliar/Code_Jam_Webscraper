#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	int T=1,n;
	cin>>n;
	while(T<=n)
	{
		//cout<<"Test case #"<<T<<"\n";
		int N,M;		
		cin>>N>>M;
		//cout<<"N = "<<N<<" M = "<<M<<"\n";
		
		int a[100][100];

		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				cin>>a[i][j];
			}
		}

		if( N==1 || M==1)
		{
			cout<<"Case #"<<T<<": YES"<<"\n";
			T++;
			continue;
		}

		int flag=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				flag = 0;
				//cout<<"a[i][j] = "<<a[i][j]<<"\n";
				for(int k=0;k<M;k++)
				{
					if (a[i][k]>a[i][j])
					{
						flag++;
						break;
					}
				}
				for(int k=0;k<N;k++)
				{
					if (a[k][j]>a[i][j])
					{
						flag++;
						break;
					}
				}
				//cout<<"flag = "<<flag<<"\n";
				if (flag==2)
					break;
			}
			if(flag==2)
				break;
		}
		if (flag==2)
			cout<<"Case #"<<T<<": NO"<<"\n";
		else
			cout<<"Case #"<<T<<": YES"<<"\n";
		T++;
	}
}
