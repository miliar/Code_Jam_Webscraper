#include <iostream>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("Magic Trick.out", "w", stdout);

	int T,A1,A[4][4],R[4];
	int r=0,n;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		r=0;
		cin>>A1;
		A1--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin>>A[j][k];
			}
		}
		for (int j = 0; j < 4; j++)
		{
			R[j]=A[A1][j];
		}
		cin>>A1;
		--A1;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin>>A[j][k];
			}
		}
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (R[j]==A[A1][k])
				{
					r++;
					n=R[j];
				}
			}
		}
		if (r==1)
		{
			cout<<"Case #"<<i+1<<": "<<n<<endl;
		}
		else if(r>1)
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else if(r==0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;

	}
}