#include <conio.h>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
//Damn bad code -.- none sleep =(
using namespace std;
void main(void)
{
  string text;
  int test;
  ifstream file; 
  ofstream Zieldatei("E:\\lo.txt");  


  file.open("E:\\test.txt", ios::in); 
  {    
      getline(file, text); 
	  test = atoi(text.c_str()) ;
  }

int ak =1;
int game[4][4];
do{
	getline(file, text);

	game[0][0]=text[0];
	game[0][1]=text[1];
	game[0][2]=text[2];
	game[0][3]=text[3];
	getline(file, text);
	game[1][0]=text[0];
	game[1][1]=text[1];
	game[1][2]=text[2];
	game[1][3]=text[3];
	getline(file, text);
	game[2][0]=text[0];
	game[2][1]=text[1];
	game[2][2]=text[2];
	game[2][3]=text[3];
	getline(file, text);
	game[3][0]=text[0];
	game[3][1]=text[1];
	game[3][2]=text[2];
	game[3][3]=text[3];
	
	char solution;
	bool nichtVoll= false;
	for(int i = 0;i<4;i++)
	{
		for(int b = 0;b<4;b++)
		{
			if(game[i][b]=='.')
			{
				nichtVoll = true;
			}
		}
	}

		for(int i = 0;i<4;i++)
		{
			int anzahlX=0;
			int anzahlO=0;
			bool joker = false;
			for(int b = 0;b<4;b++)
			{	
				if(game[i][b]=='X')
				{
					anzahlX++;
				}
				if(game[i][b]=='O')
				{
					anzahlO++;
				}
				if(game[i][b]=='T')
				{
					joker=true;
				}
			}
			if(anzahlX==4||anzahlX==3&&joker)
			{
				solution ='X';
				break;
			}
			if(anzahlO==4||anzahlO==3&&joker)
			{
				solution ='O';
				break;
			}
		}
		for(int i = 0;i<4;i++)
		{
			int anzahlX=0;
			int anzahlO=0;
			bool joker = false;
			for(int b = 0;b<4;b++)
			{	
				if(game[b][i]=='X')
				{
					anzahlX++;
				}
				if(game[b][i]=='O')
				{
					anzahlO++;
				}
				if(game[b][i]=='T')
				{
					joker=true;
				}
			}
			if(anzahlX==4||anzahlX==3&&joker)
			{
				solution ='X';
				break;
			}
			if(anzahlO==4||anzahlO==3&&joker)
			{
				solution ='O';
				break;
			}
		}
			int anzahlX=0;
			int anzahlO=0;
			bool joker = false;	
			if(game[0][0]=='X')anzahlX++;
			if(game[1][1]=='X')anzahlX++;
			if(game[2][2]=='X')anzahlX++;
			if(game[3][3]=='X')anzahlX++;

			if(game[0][0]=='O')anzahlO++;
			if(game[1][1]=='O')anzahlO++;
			if(game[2][2]=='O')anzahlO++;
			if(game[3][3]=='O')anzahlO++;

			if(game[0][0]=='T')joker = true;
			if(game[1][1]=='T')joker = true;
			if(game[2][2]=='T')joker = true;
			if(game[3][3]=='T')joker = true;
			if(anzahlX==4||anzahlX==3&&joker)
			{
				solution ='X';
				
			}
			if(anzahlO==4||anzahlO==3&&joker)
			{
				solution ='O';
			}
			 anzahlX=0;
			 anzahlO=0;
			 joker = false;	
			if(game[3][0]=='X')anzahlX++;
			if(game[2][1]=='X')anzahlX++;
			if(game[1][2]=='X')anzahlX++;
			if(game[0][3]=='X')anzahlX++;

			if(game[3][0]=='O')anzahlO++;
			if(game[2][1]=='O')anzahlO++;
			if(game[1][2]=='O')anzahlO++;
			if(game[0][3]=='O')anzahlO++;

			if(game[3][0]=='T')joker = true;
			if(game[2][1]=='T')joker = true;
			if(game[1][2]=='T')joker = true;
			if(game[0][3]=='T')joker = true;
			if(anzahlX==4||anzahlX==3&&joker)
			{
				solution ='X';
				
			}
			if(anzahlO==4||anzahlO==3&&joker)
			{
				solution ='O';
				
			}
	
	if(solution!='O'&&solution!='X'&&nichtVoll==false)
	{
		solution='d';
	}
	else if(solution!='O'&&solution!='X'&&nichtVoll==true)
	{
		solution='n';
	}


	switch(solution)
	{
	case 'n':
		Zieldatei << "Case #"<<ak <<": Game has not completed\n";
		//printf("Case #%i: Game has not completed\n",ak);
		break;
	case 'd':
				Zieldatei << "Case #"<<ak <<": Draw\n";
	//	printf("Case #%i: Draw\n",ak);
		break;
	case 'X':Zieldatei << "Case #"<<ak <<": X won\n";
		//printf("Case #%i: X won\n",ak);
		break;
	case 'O': Zieldatei << "Case #"<<ak <<": O won\n";
		//printf("Case #%i: O won\n",ak);
		break;
	}
	solution=NULL;
	if(ak==test)break;	
	ak++;
	getline(file, text);

}while(!file.eof());
  file.close();
  Zieldatei.close();
	getch();
}