#include <iostream.h>
#include <fstream.h>
#include <conio.h>
int main()
{
	clrscr();
	cout<<"\n";
	fstream input("input123.in", ios::in);
	ofstream output("Arvind1.in", ios::out);
	int loops;
	int count;
	input>>loops;
	for (int i=0; i<loops; ++i)
	{
		count=0;
		int row1;
		int row2;
		int array1[4][4];
		int array2[4][4];
		int matches[4];
		input>>row1;
		row1=row1-1;
		for (int j=0; j<4; ++j)
		{
			for (int k=0; k<4; ++k)
			{
				input>>array1[j][k];
			}
		}
		input>>row2;
		row2=row2-1;
		for (int a=0; a<4; ++a)
		{
			for (int b=0; b<4; ++b)
			{
				input>>array2[a][b];
			}
		}
		for (int c=0; c<4; ++c)
		{
			for (int d=0; d<4; ++d)
			{
				if (array1[row1][c]==array2[row2][d])
				{
				matches[count]=array1[row1][c];
				++count;
				}
			}
		}
		if (count==0)
		{
			output<<"Case #"<<i+1<<": Volunteer Cheated!\n";
		}
		else if (count==1)
		{
			output<<"Case #"<<i+1<<": "<<matches[0]<<"\n";
		}
		else if (count>1)
		{
			output<<"Case #"<<i+1<<": Bad Magician!\n";
		}
	}
	input.close();
	output.close();
	cout<<"Success!";
	getch();
	return 0;
}
