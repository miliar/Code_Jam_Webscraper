#include <string>
#include <fstream>
#include <iostream>
#define n 4

char a[n][n];
int checkx,checko,checkp;

void main()
{
	std::string s;
	
	std::fstream in("test.txt");
	std::fstream out("out.txt");
	int T;
	in>>T;
	for (int m=0; m<T;m++)
	{
		s="";
		checkx=checko=checkp=0;
		for (int i = 0; i<n; i++)
			{
				checko=checkx=0;
				for(int j = 0; j<n; j++)
			{
				in>>a[i][j];
				if (a[i][j]=='X')
					checkx++;
				if(a[i][j]=='O')
					checko++;
				if(a[i][j]=='.')
					checkp++;
				if(a[i][j]=='T')
					{
						if(checkx==3)
							checkx++;
						if(checko==3)
							checko++;
					}
				if(checkx==4)
					s="X won";
				if(checko==4)
					s="O won";
				
		}}
			if(((a[0][0]=='X')||(a[0][0]=='T'))&&
				((a[1][1]=='X')||(a[1][1]=='T'))&&
				((a[2][2]=='X')||(a[2][2]=='T'))&&
				((a[3][3]=='X')||(a[3][3]=='T')))
				s="X won";
			if(((a[0][0]=='O')||(a[0][0]=='T'))&&
				((a[1][1]=='O')||(a[1][1]=='T'))&&
				((a[2][2]=='O')||(a[2][2]=='T'))&&
				((a[3][3]=='O')||(a[3][3]=='T')))
				s="O won";
			if(((a[0][3]=='X')||(a[0][3]=='T'))&&
				((a[1][2]=='X')||(a[1][2]=='T'))&&
				((a[2][1]=='X')||(a[2][1]=='T'))&&
				((a[3][0]=='X')||(a[3][0]=='T')))
				s="X won";
			if(((a[0][3]=='O')||(a[0][3]=='T'))&&
				((a[1][2]=='O')||(a[1][2]=='T'))&&
				((a[2][1]=='O')||(a[2][1]=='T'))&&
				((a[3][0]=='O')||(a[3][0]=='T')))
				s="O won";
			for (int k=0; k<n; k++)
			{
				if(((a[0][k]=='X')||(a[0][k]=='T'))&&
					((a[1][k]=='X')||(a[1][k]=='T'))&&
					((a[2][k]=='X')||(a[2][k]=='T'))&&
					((a[3][k]=='X')||(a[3][k]=='T')))
					s="X won";
			if(((a[0][k]=='O')||(a[0][k]=='T'))&&
				((a[1][k]=='O')||(a[1][k]=='T'))&&
				((a[2][k]=='O')||(a[2][k]=='T'))&&
				((a[3][k]=='O')||(a[3][k]=='T')))
					s="O won";
			}

			if(s=="")
			{
				if(checkp!=0)
					s="Game has not completed";
				else 
					s="Draw";
			}


			out<<"Case #"<<m+1<<": "<<s<<std::endl;
	}
	getchar();
	getchar();
}
