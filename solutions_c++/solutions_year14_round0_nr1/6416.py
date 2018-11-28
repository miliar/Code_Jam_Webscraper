#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int i;
	int n;
	ifstream ist("input.in");
	ist >> n;
	ofstream ost("output.out");
	for (i = 0;i<n;i++)
	{
		int lines1,lines2;
		int matrix1[4][4];
		int matrix2[4][4];
		int answer = -1;
		bool cheated = false;
		ist >> lines1;
		for (int i1 = 0;i1<4;i1++)
			for (int i2 = 0;i2<4;i2++)
			{
				ist>>matrix1[i1][i2];
			}

		ist >>lines2;
		for (int i1 = 0;i1<4;i1++)
			for (int i2 = 0;i2<4;i2++)
			{
				ist>>matrix2[i1][i2];
			}
		for (int i1 = 0;i1<4;i1++)
			for (int i2 = 0;i2 < 4; i2++)
			{
				if (matrix1[lines1-1][i1] == matrix2[lines2-1][i2])
				{
					if (answer == -1) answer = matrix1[lines1-1][i1];
					else {cheated = true;}
				}
			}
			ost<<"Case #"<<i+1<<": ";
			if ((!cheated)&&(answer != -1)) ost<<answer<<endl;
			if (answer == -1) ost<<"Volunteer cheated!"<<endl;
			if (cheated) ost<<"Bad magician!"<<endl;
	}
}