#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int cases;
char input[4][4];
int compute()
{
	int count=0;
	for(int i=0;i<4;i++)
	{
		count=0;
		for(int j=0;j<4;j++)
		{
			if(input[i][j]=='X'|| input[i][j]=='T')
				count++;
		}
			if(count==4)
				return(2);
	}
	for(int i=0;i<4;i++)
	{
		count=0;
		for(int j=0;j<4;j++)
		{
			if(input[j][i]=='X'|| input[j][i]=='T')
				count++;
		}
			if(count==4)
				return(2);
	}
	if((input[0][0]=='X'||input[0][0]=='T')&&(input[1][1]=='X'||input[1][1]=='T')&&(input[2][2]=='X'||input[2][2]=='T')&&(input[3][3]=='X'||input[3][3]=='T'))
		return(2);
	if((input[0][3]=='X'||input[0][3]=='T')&&(input[1][2]=='X'||input[1][2]=='T')&&(input[2][1]=='X'||input[2][1]=='T')&&(input[3][0]=='X'||input[3][0]=='T'))
	    return(2);

	
	for(int i=0;i<4;i++)
	{
		count=0;
		for(int j=0;j<4;j++)
		{
			if(input[i][j]=='O'|| input[i][j]=='T')
				count++;
		}
			if(count==4)
				return(3);
	}
	for(int i=0;i<4;i++)
	{
		count=0;
		for(int j=0;j<4;j++)
		{
			if(input[j][i]=='O'|| input[j][i]=='T')
				count++;
		}
			if(count==4)
				return(3);
	}
	if((input[0][0]=='O'||input[0][0]=='T')&&(input[1][1]=='O'||input[1][1]=='T')&&(input[2][2]=='O'||input[2][2]=='T')&&(input[3][3]=='O'||input[3][3]=='T'))
		return(3);
	if((input[0][3]=='O'||input[0][3]=='T')&&(input[1][2]=='O'||input[1][2]=='T')&&(input[2][1]=='O'||input[2][1]=='T')&&(input[3][0]=='O'||input[3][0]=='T'))
	    return(3);
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(input[i][j]=='.')
				return(1);
	return(0);
}
int main()
{
	int res;
	fin>>cases;
	int k=0;
	while(k<cases)
	{
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				fin>>input[i][j];
		fout<<"Case #";
		fout<<k+1;
		fout<<": ";
		res=compute();
		switch(res)
		{
			case 0 : fout<<"Draw";
					 break;
			case 1 : fout<<"Game has not completed";
					 break;
			case 2 : fout<<"X won";
					  break;
			case 3 : fout<<"O won";
				  
		}
		k++;
		if(k!=cases){fout<<"\n";}
	}
	return 0;
}

