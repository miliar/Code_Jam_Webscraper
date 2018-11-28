#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	//ifstream inputReader("A-small-attempt0.in");
	//ofstream outputWriter("outputA.out");

	int T;
	cin>>T;

	for (int t = 0; t < T; t++)
	{
		int m,n;
		int a[4][4], b[4][4];
		cin>>m;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>a[i][j];
			}
		}

		cin>>n;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>b[i][j];
			}
		}

		//Check how any numbers from row m of matrix a are in row n of matrix b
		int count = 0;
		int answer = -1;
		for (int i = 0; i < 4; i++)
		{
			int numInAatRowM = a[m-1][i];
			for (int j = 0; j < 4; j++)
			{
				if(b[n-1][j] == numInAatRowM)
				{
					count++;
					if(count == 1)
						answer = numInAatRowM;
					break;
				}
			}
		}

		if(count == 0)
		{
			cout<<"Case #"<<t+1<<": Volunteer cheated!"<<endl;
		}
		else if(count == 1)
		{
			cout<<"Case #"<<t+1<<": "<<answer<<endl;
		}
		else
		{
			cout<<"Case #"<<t+1<<": Bad magician!"<<endl;
		}
	}
	//outputWriter.close();
	return 0;
}