#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{


	ifstream handle;
	ofstream out;
	out.open("output.txt",ios::out);
	handle.open("input.in",ios::in);
   int xcount=0;
   int ycount=0;
   int tcount=0;
   int dotcount=0;
   bool breakcheck=false;
   char line[200];
   handle.getline(line,200,'\n');
   int test=atoi(line);
   char *board[4];
   for(int d=0;d<4;d++)
   {
		board[d]=new char[5];


   }
   for(int i=1;i<=test;i++)
   {
	   xcount=0;ycount=0;tcount=0;dotcount=0;
	breakcheck=false;
	if(i>1)
	{
		handle.getline(line,200,'\n');
	}
	for(int j=0;j<4;j++)
	{
	handle.getline(line,200,'\n');
	strcpy(board[j],line);
	cout<<line<<endl;
	}
cout<<endl<<endl;
	
	for( int y=0;y<4;y++)
	{
		xcount=0;ycount=0;tcount=0;

		for(int u=0;u<4;u++)
		{
			if(board[y][u]=='X')
			{
				xcount++;
			
			}
			else if(board[y][u]=='O')
			{
				ycount++;
			}
			else if(board[y][u]=='T')
			{

				tcount++;
			}
			else if(board[y][u]=='.')
			{
				dotcount++;
			}


		}
	//	cout<<xcount<<endl<<ycount<<endl;
	//	system("pause");
		if(xcount==4)
		{
				cout<<"Case #"<<i<<": "<<"X won"<<endl;
				out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
				break;

		}
		else if(ycount==4)
		{
			cout<<"Case #"<<i<<": "<<"O won"<<endl;
		out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
			break;

		}
		else if(xcount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"X won"<<endl;
			out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
				break;

		}
		else if(ycount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"O won"<<endl;
			out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
			break;
		}

	}
		if(breakcheck==true)
		{
			continue;
		}


			xcount=0;ycount=0;
	for( int q=0;q<4;q++)
	{
		xcount=0;ycount=0;tcount=0;

		for(int w=0;w<4;w++)
		{
			if(board[w][q]=='X')
			{
				xcount++;
			
			}
			else if(board[w][q]=='O')
			{
				ycount++;
			}
			else if(board[w][q]=='T')
			{

				tcount++;
			}
			else if(board[w][q]=='.')
			{
				dotcount++;
			}


		}
	//	cout<<xcount<<endl<<ycount<<endl;
	//	system("pause");
		if(xcount==4)
		{
				cout<<"Case #"<<i<<": "<<"X won"<<endl;
				out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
				break;

		}
		else if(ycount==4)
		{
			cout<<"Case #"<<i<<": "<<"O won"<<endl;
			out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
			break;

		}
		else if(xcount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"X won"<<endl;
		out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
				break;

		}
		else if(ycount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"O won"<<endl;
		out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
			break;
		}

	}
	if(breakcheck==true)
		{
			continue;
		}
	xcount=0;ycount=0;tcount=0;
	int z=0;int x=0;
	for( z=0,x=0;z<4,x<4;z++,x++)
	{
	
		if(board[z][x]=='O')
		{
			ycount++;
		}
		else if(board[z][x]=='X')
		{
			xcount++;
		}
		else if(board[z][x]=='T')
		{
			tcount++;
		}
			else if(board[z][x]=='.')
		{
			dotcount++;
		}


	}

	//	cout<<ycount<<"case "<<i;
	if(xcount==4)
		{
				cout<<"Case #"<<i<<": "<<"X won"<<endl;
					out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
				//break;

		}
		else if(ycount==4)
		{
			cout<<"Case #"<<i<<": "<<"O won"<<endl;
				out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
		//	break;

		}
		else if(xcount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"X won"<<endl;
		out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
			//	break;

		}
		else if(ycount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"O won"<<endl;
			out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
		//	break;
		}
	if(breakcheck==true)
		{//cout<<i;
			continue;
		}
	xcount=0;ycount=0;tcount=0;
		for( z=0,x=3;z<4;z++,x--)
	{
	
		if(board[z][x]=='O')
		{
			ycount++;
		}
		else if(board[z][x]=='X')
		{
			xcount++;
		}
		else if(board[z][x]=='T')
		{
			tcount++;
		}
			else if(board[z][x]=='.')
		{
			dotcount++;
		}


	}
	
	if(xcount==4)
		{
				cout<<"Case #"<<i<<": "<<"X won"<<endl;
				out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
				//break;

		}
		else if(ycount==4)
		{
			cout<<"Case #"<<i<<": "<<"O won"<<endl;
				out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
		//	break;

		}
		else if(xcount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"X won"<<endl;
			out<<"Case #"<<i<<": "<<"X won"<<endl;
				breakcheck=true;
			//	break;

		}
		else if(ycount==3&&tcount==1)
		{
		cout<<"Case #"<<i<<": "<<"O won"<<endl;
			out<<"Case #"<<i<<": "<<"O won"<<endl;
			breakcheck=true;
		//	break;
		}
		if(breakcheck==true)
		{//cout<<i;
			continue;
		}
		if(dotcount==0)
		{
			cout<<"Case #"<<i<<": "<<"Draw"<<endl;
			out<<"Case #"<<i<<": "<<"Draw"<<endl;
		}
		else if(dotcount>0)
		{
cout<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
out<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
		}




   }
 
handle.close();
out.close();
	return 0;
}