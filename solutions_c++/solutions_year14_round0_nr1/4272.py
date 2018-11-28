#include<iostream>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int probcount;
	cin>>probcount;

	int mat1[4][4];
	int mat2[4][4];

	for (int i=0 ; i<probcount ; i++)
	{
		int ans1,ans2;

		cin>>ans1;	//Matrix 1 input
		for (int v=0 ; v<4 ; v++)
		{
			for (int j=0 ; j<4 ; j++)
			{
				cin>>mat1[v][j];
			}
		}

		cin>>ans2;	//Matrix 2 input
		for (int v=0 ; v<4 ; v++)
		{
			for (int j=0 ; j<4 ; j++)
			{
				cin>>mat2[v][j];
			}
		}

		//Solution
		int flag=0;
		int finalans;

		for (int v=0 ; v<4 ; v++)
		{
			for (int j=0 ; j<4 ; j++)
			{
				if (mat1[ans1-1][v] == mat2[ans2-1][j])
				{
					flag++;
					finalans=mat1[ans1-1][v];
				}
			}
		}

		if (flag == 0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if (flag == 1)
			cout<<"Case #"<<i+1<<": "<<finalans<<endl;
		else
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
}