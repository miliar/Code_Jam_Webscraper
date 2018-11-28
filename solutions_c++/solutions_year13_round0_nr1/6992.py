//============================================================================
// Name        : CodeJam1.cpp
// Author      : Fabho
// Version     :
// Copyright   : Copyleft
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
char mat[5][5];
void init(){
string sal = "",cad;
	for(int a=1; a<=4;a++)
	   {
		getline(cin,cad);
		sal+=cad;
	   }
int index =0;
for(int x=0; x<4; x++)
	for(int y=0; y<4; y++)
	    {
		 mat[x][y] = sal[index];
		 index++;
	    }
getline(cin,cad);
}
void print(){
	for(int f=0; f<4; f++)
	   {
		for(int g=0; g<4; g++)
		   {
			cout<<mat[f][g];
		   }
		cout<<endl;
	   }
}
int main() {
int casos,find,xc,yc,tok;
string trash;
cin>>casos;
getline(cin,trash);
for(int d=1; d<=casos; d++)
{
init();
find =0;
xc = yc = tok = 0;
for(int x=0; x<4; x++)
   {
	xc = yc = tok = 0;
	for(int y=0; y<4; y++)
	   {
	    if(mat[x][y] == 'X')
	    	xc++;
	    else if(mat[x][y] == 'O')
	    	    yc++;
	    else if(mat[x][y] == 'T')
	    	    tok = 1;
	    else//Se encuentra punto
	    	break;
	   }
	  if((xc == 3 && tok ==1) || xc ==4)
		 {
		  cout<<"Case #"<<d<<": X won\n";
		  find = 1;
		  break;
		 }
	  else if((yc == 3 && tok == 1) || yc == 4)
	          {
		       cout<<"Case #"<<d<<": O won\n";
	           find  = 1;
	           break;
	          }
   }
	if(find == 0) // Recorrer columnas
	  {
		for(int x=0; x<4; x++)
		   {
			xc = yc = tok = 0;
			for(int y=0; y<4; y++)
			   {
			    if(mat[y][x] == 'X')
			    	xc++;
			    else if(mat[y][x] == 'O')
			    	    yc++;
			    else if(mat[y][x] == 'T')
			    	    tok = 1;
			    else//Se encuentra punto
			    	break;
			   }
			  if((xc == 3 && tok ==1) || xc ==4)
				 {
				  cout<<"Case #"<<d<<": X won\n";
				  find = 1;
				  break;
				 }
			  else if((yc == 3 && tok == 1) || yc == 4)
			          {
				       cout<<"Case #"<<d<<": O won\n";
			           find  = 1;
			           break;
			          }
		   }
	  }
	if(find == 0)
	  {
		xc = yc = tok = 0;
		for(int a=0; a<4; a++)
		   {
			if(mat[a][a] == 'X')
			   xc++;
			else if(mat[a][a] == 'O')
				    yc++;
			else if(mat[a][a] == 'T')
			 	    tok = 1;
			else//Se encuentra punto
				break;
		   }
		  if((xc == 3 && tok ==1) || xc ==4)
			 {
			  cout<<"Case #"<<d<<": X won\n";
			  find = 1;
			 }
		  else if((yc == 3 && tok == 1) || yc == 4)
		          {
			       cout<<"Case #"<<d<<": O won\n";
		           find  = 1;
		          }
	  }
	if(find == 0)
	  {
		xc = yc = tok = 0;
		for(int a=0,b=3; a<4; a++,b--)
		   {
			if(mat[a][b] == 'X')
			   xc++;
			else if(mat[a][b] == 'O')
				    yc++;
			else if(mat[a][b] == 'T')
			 	    tok = 1;
			else//Se encuentra punto
				break;
		   }
		  if((xc == 3 && tok ==1) || xc ==4)
			 {
			  cout<<"Case #"<<d<<": X won\n";
			  find = 1;
			 }
		  else if((yc == 3 && tok == 1) || yc == 4)
		          {
			       cout<<"Case #"<<d<<": O won\n";
		           find  = 1;
		          }
	  }
/****************************************Toca empate o juego no acabado*/
	  if(find == 0)
	    {
		  for(int a=0;a<4; a++)
		     {
			  for(int b=0; b<4; b++)
			     {
				  if(mat[a][b] == '.'){
					 cout<<"Case #"<<d<<": Game has not completed\n";
				     find = 1;
				     break;
				    }
			     }
			  if(find == 1)
				 break;
		     }
		   if(find == 0)
			   cout<<"Case #"<<d<<": Draw\n";
	    }
}//casos
return 0;
}
