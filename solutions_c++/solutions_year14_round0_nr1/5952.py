#include<iostream>

using namespace std;

int intersect(int a[], int b[], int &number)
{
	int ret = 0;
	for(int i = 0;i < 4;i++)
	{
		for (int j = 0;j < 4;j++)
		{
			if(a[i] == b[j])
			{
				number = a[i];
				ret ++;
				break;
			}
		}
	}

	return ret;
}



void main()
{
	int T;
	cin>>T;
	for(int i = 0; i < T;i++)
	{
		int firstRow;
		cin>>firstRow;

		int matrix[4][4];
		for(int j = 0;j < 4;j ++)
		{
			for(int k = 0;k < 4;k++)
			{
				cin >> matrix[j][k];	
			}
		}
		
		int secondRow;
		cin >>secondRow;

		int rmatrix[4][4];
		for(int j = 0;j < 4;j ++)
		{
			for(int k = 0;k < 4;k++)
			{
				cin >> rmatrix[j][k];	
			}
		}
		int number = 0;
		int ret = intersect(matrix[firstRow - 1], rmatrix[secondRow - 1], number);
		
		cout<<"Case #"<<(i+1)<<": ";
		if (ret == 1)
		{
			cout<<number;
		}
		else if(ret == 0)
		{
			cout<<"Volunteer cheated!";
		}
		else
		{
			cout<<"Bad magician!";
		}
		cout<<endl;
	}

}