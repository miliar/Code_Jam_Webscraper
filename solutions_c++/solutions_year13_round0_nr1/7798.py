#include<fstream>
#include<iostream>
using namespace std;
int main()
{
char a[4][4];char W;
int T=0;
ifstream in;
ofstream out;
out.open("out.txt");
in.open("A-small-attempt0.in");
in>>T;
cout<<T;
int n=0,g=-1;
while(!in.eof())

{
	n++;g=-1;
	if(n>T)
	break;	
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		{
		in>>a[i][j];
//		cout<<a[i][j];
		}
	g=-1;
	
	W='O';
if(g!=0)
	{
	for(int i=0;i<2;i++)
	{
	for(int j=0;j<4;j++)
		{
		if(((a[j][0]==W ||a[j][0]=='T')&&(a[j][1]==W ||a[j][1]=='T')&&(a[j][2]==W ||a[j][2]=='T')&&(a[j][3]==W ||a[j][3]=='T'))||((a[0][j]==W ||a[0][j]=='T')&&(a[1][j]==W ||a[1][j]=='T')&&(a[2][j]==W ||a[2][j]=='T')&&(a[3][j]==W ||a[3][j]=='T')))
			{
			if(W=='O')
		 	g=1;
			else 
			g=2;
		  	break;	
			}
		
		}
	if(((a[0][0]==W ||a[0][0]=='T')&&(a[1][1]==W ||a[1][1]=='T')&&(a[2][2]==W ||a[2][2]=='T')&&(a[3][3]==W ||a[3][3]=='T'))||((a[0][3]==W ||a[0][3]=='T')&&(a[1][2]==W ||a[1][2]=='T')&&(a[2][1]==W ||a[2][1]=='T')&&(a[3][0]==W ||a[3][0]=='T')))
		{
		if(W=='O')
	 	g=1;
		else 
		g=2;
		
		break;	
		}
	W='X';
	}
}if(g==-1)
for(int i=0;i<4;i++)
		{
		for(int j=0;j<4;j++)
			{
			if(a[i][j]=='.'){
			g=0;break;
				}
			} 
		if(g==0)
		break;			
		}
out<<"Case #"<<n<<": "; 
if(g==0)
out<<"Game has not completed"<<endl;
else if(g==1)
out<<"O won"<<endl;
else if(g==2)
out<<"X won"<<endl;
else out<<"Draw"<<endl;
}

}
