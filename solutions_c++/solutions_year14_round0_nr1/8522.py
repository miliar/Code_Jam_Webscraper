# include "iostream"
# include "fstream"
using namespace std;

void main()
{
	ifstream inf("A-small-attempt0.in", ios::in);
	ofstream outf("A-small.out", ios::out);
	int test = 0;
	int row1 = 0;
	int row2 = 0, count = 0;
	int card = 0;

	int **matrix1 = new int* [4];

	for(int i = 0; i<4; i++)
	{
		matrix1[i] = new int[4];
	}
	

	int **matrix2 = new int* [4];
	
	for(int i = 0; i<4; i++)
	{
		matrix2[i] = new int[4];
	}

	inf>>test;

	for (int m = 0; m<test; m++)
	{
		count = 0;
		inf>>row1;
		for(int row = 0; row<4; row++)
		{
			for(int col = 0; col<4; col++)
			{
				inf>>matrix1[row][col];
			}
		}


		inf>>row2;
		for(int row = 0; row<4; row++)
		{
			for(int col = 0; col<4; col++)
			{
				inf>>matrix2[row][col];
			}
		}
		

		for(int i= 0; i<4; i++)
		{
			for(int j= 0; j<4; j++)
			{
				if(matrix1[row1-1][i] == matrix2[row2-1][j] )
				{
					card = matrix1[row1-1][i];
					count++;
				}
			}
		}


		if(count >1)
		{
			outf<<"Case #"<<m+1<<": Bad magician!"<<endl;
			
		}

		if(count==0)
		{
			outf<<"Case #"<<m+1<<": Volunteer Cheated!"<<endl;
		}

		if(count==1)
		{
			outf<<"Case #"<<m+1<<": "<<card<<endl;
		}
	}
	
	inf.close();
	outf.close();

}