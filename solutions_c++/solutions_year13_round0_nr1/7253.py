# include <fstream>
# include <iostream>
# define DIM 1003
using namespace std;
int t, ast[8][8], as[8][8], adr[8][8], bst[8][8], bs[8][8], bdr[8][8], la[8], lb[8];
char c[8];

void upda(int i, int j)
{
	ast[i][j+1]=ast[i-1][j]+1;
	as[i][j+1]=as[i-1][j+1]+1;
	adr[i][j+1]=adr[i-1][j+2]+1;
	la[j+1]=la[j]+1;
}

void updb(int i, int j)
{
	bst[i][j+1]=bst[i-1][j]+1;
	bs[i][j+1]=bs[i-1][j+1]+1;
	bdr[i][j+1]=bdr[i-1][j+2]+1;
	lb[j+1]=lb[j]+1;
}

int main()
{
	ifstream fin ("f.in");
	ofstream fout ("f.out");
	
	fin>>t;
	fin.get();

	for(int nt=1;nt<=t;++nt)
	{
		int ra = 0, rb = 0, dr=0;
		for(int i=1;i<=4;++i)
		{
			fin.getline(c, 6);
			
			for(int j=0;j<4;++j)
			{
				if (c[j]=='.')
				{
					++dr;
					ast[i][j+1]=as[i][j+1]=adr[i][j+1]=la[j+1]=0;
					bst[i][j+1]=bs[i][j+1]=bdr[i][j+1]=lb[j+1]=0;
				}
				else if (c[j]=='X')
				{
					upda(i, j);
					bst[i][j+1]=bs[i][j+1]=bdr[i][j+1]=lb[j+1]=0;
				}
				else if (c[j]=='O')
				{
					updb(i, j);
					ast[i][j+1]=as[i][j+1]=adr[i][j+1]=la[j+1]=0;
				}
				else if (c[j]=='T')
				{
					upda(i, j);
					updb(i, j);
				}
				
				if (ast[i][j+1]==4 || as[i][j+1]==4 || adr[i][j+1]==4 || la[j+1]==4)
				{
					++ra;
				}
				if (bst[i][j+1]==4 || bs[i][j+1]==4 || bdr[i][j+1]==4 || lb[j+1]==4)
				{
					++rb;	
				}
			}
		}
		
		fout<<"Case #"<<nt<<": ";
		if (ra && !rb)
			fout<<"X won\n";
		else if (!ra && rb)
			fout<<"O won\n";
		else if (!ra && !rb)
		{
			if (!dr)
				fout<<"Draw\n";
			else
				fout<<"Game has not completed\n";
		}
		else if (ra && rb)
			fout<<"Draw\n";
		
		fin.get();
	}
	
	return 0;
}
		
