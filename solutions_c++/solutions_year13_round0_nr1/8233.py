#include<iostream>
#include<fstream>
using namespace std;

char game[4][4];

int incomplete();
int check();
int row_x();
int col_x();
int diag_x();
int row_o();
int col_o();
int diag_o();


int main()
{
   ifstream read;
   ofstream write;
   write.open("small.in",ios::out);
   read.open("i.in",ios::in);

   int x;
   read>>x;

   char a;
   int status=0;
	for(int i=1; i<=x; i++)
	{
  		for(int k=0; k<4; k++)
		{
			for(int j=0; j<4; j++)
			{
			   read>>a;
			   game[k][j]=a;
			}
		}

		status=check();
		if(status==1)
        write<<"Case #"<<i<<": X won\n";
        else if(status==2)
        write<<"Case #"<<i<<": O won\n";
        else if(status==3)
        write<<"Case #"<<i<<": Game has not completed\n";
        else if(status==4)
        write<<"Case #"<<i<<": Draw\n";
	}
 	return 0;
}


int check()
{   int start=0;
    start=row_x();
    if(start==1)
    return 1;
    start=col_x();
    if(start==1)
    return 1;
    start=diag_x();
    if(start==1)
    return 1;

     start=0;
    start=row_o();
    if(start==1)
    return 2;
    start=col_o();
    if(start==1)
    return 2;
    start=diag_o();
    if(start==1)
    return 2;

    start=incomplete();
    if(start==1)
    return 3;

    if(start==0)
    return 4;
}

int row_x()
{
     int c=0;
	for(int i=0; i<4; i++)
	{   if(c==4)
	    break;
	    else c=0;
	    for(int j=0; j<4; j++)
        {
            if(game[i][j]=='X' || game[i][j]=='T')
                c++;

        }
	}
	if(c==4)
    return 1;
    else return 0;
}

int col_x()
{
     int c=0;
	for(int i=0; i<4; i++)
	{   if(c==4)
	    break;
	    else c=0;
	    for(int j=0; j<4; j++)
        {
            if(game[j][i]=='X' || game[j][i]=='T')
                c++;

        }
	}
	if(c==4)
    return 1;
    else return 0;
}

int diag_x()
{
    int c=0;


    for(int j=0; j<4; j++)
    {
            if(game[j][j]=='X' || game[j][j]=='T')
            c++;
    }
    if(c==4)
    return 1;
    else c=0;
    int j=0;
    for(int i=3; i>-1; i--)
    {
         if(game[i][j]=='X' || game[i][j]=='T')
         c++;
         j++;
    }
    if(c==4)
    return 1;
    else return 0;

}


int row_o()
{
     int c=0;
	for(int i=0; i<4; i++)
	{   if(c==4)
	    break;
	    else c=0;
	    for(int j=0; j<4; j++)
        {
            if(game[i][j]=='O' || game[i][j]=='T')
                c++;

        }
	}
	if(c==4)
    return 1;
    else return 0;
}

int col_o()
{
     int c=0;
	for(int i=0; i<4; i++)
	{   if(c==4)
	    break;
	    else c=0;
	    for(int j=0; j<4; j++)
        {
            if(game[j][i]=='O' || game[j][i]=='T')
                c++;

        }
	}
	if(c==4)
    return 1;
    else return 0;
}

int diag_o()
{
    int c=0;


    for(int j=0; j<4; j++)
    {
            if(game[j][j]=='O' || game[j][j]=='T')
            c++;
    }
    if(c==4)
    return 1;
    else c=0;
    int j=0;
    for(int i=3; i>-1; i--)
    {
         if(game[i][j]=='O' || game[i][j]=='T')
         c++;
         j++;
    }
    if(c==4)
    return 1;
    else return 0;

}


int incomplete()
{
    int c=0;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(game[i][j]=='.')
                c++;
        }
    }
    if(c==0)
    return 0;
    else return 1;
}
