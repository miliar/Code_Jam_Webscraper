#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
	clrscr();
	int testcases,trials=0;
	int answer;
	int a[4][4];
	int number[4];
	ifstream fin;
	fin.open("A.in",ios::in);
	ofstream fout;
	fout.open("A.txt",ios::out);
	fin>>testcases;
	while(trials<testcases)
	{
		int row1,row2,t=0;
		fin>>row1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				fin>>a[i][j];
		for(j=0;j<4;j++)
			number[j]=a[(row1-1)][j];

		fin>>row2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fin>>a[i][j];
		for(int f=0;f<4;f++)
			for(j=0;j<4;j++)
				{
					if(number[f]==a[(row2-1)][j])
					{
						t++;
						answer=number[f];
					}
				}
		if(t==1)
			fout<<"Case #"<<trials+1<<": "<<answer<<endl;
		else if(t>1)
			fout<<"Case #"<<trials+1<<": "<<"Bad magician!"<<endl;
		else
			fout<<"Case #"<<trials+1<<": "<<"Volunteer cheated!"<<endl;
		trials++;
	}
fin.close();
getch();
}







