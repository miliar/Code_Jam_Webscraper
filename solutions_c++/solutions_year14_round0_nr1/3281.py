#include <iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int row1;
		cin>>row1;
		row1--;
		int A[4][4];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>A[j][k];
			}
		}
		int row2;
		cin>>row2;
		row2--;
		int B[4][4];
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>B[j][k];
			}
		}
		int match=0;
		int number=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(A[row1][j]==B[row2][k])
					{
						match++;
						number=A[row1][j];
					}
			}
		}
		if(match==1)
			cout<<"Case #"<<i+1<<": "<<number<<endl;
		if(match>1)
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		if(match==0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
	}
}