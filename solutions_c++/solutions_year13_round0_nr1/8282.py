#include <iostream>
using namespace std;
char map[4][4]; int answer,T;
bool point=false,xwin=false,owin=false;
void busqueda ()
{
	int I,J;
	for(I=0;I<4;I++)
	{
		if(map[I][0]=='X'&&map[I][1]=='X'&&map[I][2]=='X'&&map[I][3]=='X')
		{xwin=true;}
		if(map[I][0]=='O'&&map[I][1]=='O'&&map[I][2]=='O'&&map[I][3]=='O')
		{owin=true;}
		if(map[I][0]=='T'&&map[I][1]=='X'&&map[I][2]=='X'&&map[I][3]=='X')
		{xwin=true;}
		if(map[I][0]=='X'&&map[I][1]=='X'&&map[I][2]=='X'&&map[I][3]=='T')
		{xwin=true;}
		if(map[I][0]=='T'&&map[I][1]=='O'&&map[I][2]=='O'&&map[I][3]=='O')
		{owin=true;}
		if(map[I][0]=='O'&&map[I][1]=='O'&&map[I][2]=='O'&&map[I][3]=='T')
		{owin=true;}
	}
	for(J=0;J<4;J++)
	{
		if(map[0][J]=='X'&&map[1][J]=='X'&&map[2][J]=='X'&&map[3][J]=='X')
		{xwin=true;}
		if(map[0][J]=='O'&&map[1][J]=='O'&&map[2][J]=='O'&&map[3][J]=='O')
		{owin=true;}
		if(map[0][J]=='T'&&map[1][J]=='X'&&map[2][J]=='X'&&map[3][J]=='X')
		{xwin=true;}
		if(map[0][J]=='T'&&map[1][J]=='O'&&map[2][J]=='O'&&map[3][J]=='O')
		{owin=true;}
		if(map[0][J]=='X'&&map[1][J]=='X'&&map[2][J]=='X'&&map[3][J]=='T')
		{xwin=true;}
		if(map[0][J]=='O'&&map[1][J]=='O'&&map[2][J]=='O'&&map[3][J]=='T')
		{owin=true;}
	}
	if(map[0][0]=='X'&&map[1][1]=='X'&&map[2][2]=='X'&&map[3][3]=='X'){xwin=true;}
	if(map[0][0]=='X'&&map[1][1]=='X'&&map[2][2]=='X'&&map[3][3]=='T'){xwin=true;}
	if(map[0][0]=='T'&&map[1][1]=='X'&&map[2][2]=='X'&&map[3][3]=='X'){xwin=true;}
	if(map[0][0]=='O'&&map[1][1]=='O'&&map[2][2]=='O'&&map[3][3]=='O'){owin=true;}
	if(map[0][0]=='O'&&map[1][1]=='O'&&map[2][2]=='O'&&map[3][3]=='T'){owin=true;}
	if(map[0][0]=='T'&&map[1][1]=='O'&&map[2][2]=='O'&&map[3][3]=='O'){owin=true;}
	if(map[3][0]=='X'&&map[2][1]=='X'&&map[1][2]=='X'&&map[0][3]=='X'){xwin=true;}
	if(map[3][0]=='X'&&map[2][1]=='X'&&map[1][2]=='X'&&map[0][3]=='T'){xwin=true;}
	if(map[3][0]=='T'&&map[2][1]=='X'&&map[1][2]=='X'&&map[0][3]=='X'){xwin=true;}
	if(map[3][0]=='O'&&map[2][1]=='O'&&map[1][2]=='O'&&map[0][3]=='O'){owin=true;}
	if(map[3][0]=='O'&&map[2][1]=='O'&&map[1][2]=='O'&&map[0][3]=='T'){owin=true;}
	if(map[3][0]=='T'&&map[2][1]=='O'&&map[1][2]=='O'&&map[0][3]=='O'){owin=true;}
		if((point==false)&&(xwin==false)&&(owin==false)){answer=3;}
		if(xwin==true){answer=1;}
		if(owin==true){answer=2;}
		if((point==true)&&(xwin==false)&&(owin==false)){answer=4;}
}
int main ()
{
	int i,j,w;
	cin>>T;
	for(w=1;w<T+1;w++)
	{
		point=false,xwin=false,owin=false;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>map[i][j];
				if(map[i][j]=='.')
				{point = true;}
			}
		}	
		busqueda ();
		switch(answer)
		{
		case 1:
		cout<<"Case #"<<w<<": X won"<<endl;
		break;
		case 2:
		cout<<"Case #"<<w<<": O won"<<endl;
		break;
		case 3:
		cout<<"Case #"<<w<<": Draw"<<endl;
		break;
		case 4:
		cout<<"Case #"<<w<<": Game has not completed"<<endl;
		break;
		}
	}
	return 0;
}
