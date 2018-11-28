#include<string>
#include<iostream>
using namespace std;
char mat[4][4];
bool win=false;
char gana='e';
int s[2];
void pr()
{
for (int q=0;q<4;q++)
{
for (int w=0;w<4;w++)
{
cout<<mat[q][w];
}
cout<<endl;
}


}
void res(char l)
{	if (l=='X')
	{
	for(int m=0;m<4;m++){for(int g=0;g<4;g++){if(mat[m][g]=='.'){gana='.';} if(mat[m][g]=='T'){s[0]=m;s[1]=g;mat[m][g]='X';}}}
//	pr();
	for (int i=0;i<4;i++)
	{
		
	if(mat[i][0]=='X'&&mat[i][1]=='X'&&mat[i][2]=='X'&&mat[i][3]=='X'){ win=true; gana='X';}
	}
        for (int i=0;i<4;i++)
        {       
                
        if(mat[0][i]=='X'&&mat[1][i]=='X'&&mat[2][i]=='X'&&mat[3][i]=='X'){win=true; gana='X';}
        }
if(mat[0][0]=='X'&&mat[1][1]=='X'&&mat[2][2]=='X'&&mat[3][3]=='X'){win=true; gana='X';}
if(mat[3][0]=='X'&&mat[2][1]=='X'&&mat[1][2]=='X'&&mat[0][3]=='X'){win=true; gana='X';}

	}
else
	{
	
//	for(int m=0;m<4;m++){for(int g=0;g<4;g++){if(mat[m][g]=='.'){gana='.';} if(mat[m][g]=='T'){mat[m][g]='O';}}}
mat[s[0]][s[1]]='O';
//pr();
	for (int i=0;i<4;i++)
	{
		
	if(mat[i][0]=='O'&&mat[i][1]=='O'&&mat[i][2]=='O'&&mat[i][3]=='O'){win=true; gana='O';}
	}
        for (int i=0;i<4;i++)
        {       
                
        if(mat[0][i]=='O'&&mat[1][i]=='O'&&mat[2][i]=='O'&&mat[3][i]=='O'){win=true; gana='O';}
        }
if(mat[0][0]=='O'&&mat[1][1]=='O'&&mat[2][2]=='O'&&mat[3][3]=='O'){win=true; gana='O';}
if(mat[3][0]=='O'&&mat[2][1]=='O'&&mat[1][2]=='O'&&mat[0][3]=='O'){win=true; gana='O';}
	}

}
void ini()
{
	for (int i=0;i<4;i++)
	{
		gana='e';
		win=false;
		for (int j=0;j<4;j++)
		{
			mat[i][j]='.';

		}
	}
}
int main ()
{
int cas;
cin>>cas;
for (int h=1;h<=cas;h++)
{
	ini();		
	
	for (int i=0;i<4;i++)
{	for (int j=0;j<4;j++)
{cin>>mat[i][j];
}}
//cout<<"recibi: "<<endl;
//pr();
//cout<<"recibi: "<<endl;
res('X');
if (win==false){res('O');}
cout<<"Case #"<<h<<": ";
if(win){cout<<gana<<" won"<<endl;}
else{
	if (gana=='.'){cout<<"Game has not completed"<<endl;}
	else{cout<<"Draw"<<endl;}
}
}

return 0;
}
