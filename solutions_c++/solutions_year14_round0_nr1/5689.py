// Craciun Catalin
//  Google Code Jam
//   A
#include <iostream>

#define NMax 4

using namespace std;

int t;
short row1, row2;
short A[NMax][NMax], B[NMax][NMax];

void solve()
{
	int identical=0;
	int poz=0;

	for (int j=0;j<4;j++)
		for (int p=0;p<4;p++)
			if (A[row1][j]==B[row2][p])
			{
				identical++;
				poz=j;
			}
	
	if (identical==1)
		cout<<A[row1][poz];
	else if (identical==0)
		cout<<"Volunteer cheated!";
	else
		cout<<"Bad magician!";
}

int main()
{
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>row1; row1--;
		for (short k=0;k<4;k++)
			for (short kk=0;kk<4;kk++)
				cin>>A[k][kk];
		cin>>row2; row2--;
		for (short k=0;k<4;k++)
			for (short kk=0;kk<4;kk++)
				cin>>B[k][kk];
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<'\n';
	}

	return 0;
}
