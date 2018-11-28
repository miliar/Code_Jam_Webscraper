#include <string>
#include<iostream>
#include <fstream>
using namespace std;

void Judge(int a1, int mat1[][4], int a2, int mat2[][4], ofstream &of)
{
	int c=0;
	int t = 0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(mat1[a1][i]==mat2[a2][j])
			{
				c++;
				t = mat1[a1][i];
			}
		}
		
		if(c==1)
			of<<t<<endl;
		else if(c==0)
			of<<"Volunteer cheated!\n";
		else 
			of<<"Bad magician!\n";

}



#include<iomanip>
int main()
{
	ofstream of("a.txt");
	ifstream iff( "A-small-attempt1.in",ios::in );

	int n;
	iff>>n;
	int a1, a2;
	int mat1[4][4];
	int mat2[4][4];
	for(int i=0; i<n; i++)
	{
		
		iff>>a1;
		for(int r=0;r<4;r++)
			for(int c=0;c<4;c++)
				iff>>mat1[r][c];
		iff>>a2;
		for(int r=0;r<4;r++)
			for(int c=0;c<4;c++)
				iff>>mat2[r][c];
		of<<"Case #"<<i+1<<": ";
		Judge(a1-1, mat1, a2-1, mat2, of);
	}
	of.close();
	return 0;
}




