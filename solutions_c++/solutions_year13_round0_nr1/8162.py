#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;


int main()
{

	int n;
	
	string in[4];
	bool X=false;
	bool O=false;
	bool draw=false;
	bool notfinished=false;
	ofstream fout;
	ifstream fin ("A-small-attempt1.in");
	fout.open("reault.out ");
	fin>>n;

	
	//string in1,in2,in3,in4;
	for(int i=0;i<n;i++)
	{
		X=false;
	    O=false;
	    draw=false;
	    notfinished=false;

		for(int j=0;j<4;j++)
		{
			fin>>in[j];
		//	cin>>in1;
			//if(in1[0]=='X' ||( in1[0]=='X' &&in1[3]=='T') ||( in1[1]=='X' &&in1[0]=='T'))
				
			if(in[j][0]==in[j][1]&& in[j][1]==in[j][2]&& in[j][1]==in[j][3]&& in[j][1]=='X' ||(in[j][0]==in[j][1]&& in[j][1]==in[j][2]&& in[j][2]=='X' &&in[j][3]=='T') ||( in[j][1]==in[j][2]&&in[j][1]==in[j][3]&& in[j][1]=='X' &&in[j][0]=='T'))
				X=true;
			else //if(in1[0]==in1[1]==in1[2]==in1[3]=='O' ||( in1[0]==in1[1]==in1[2]=='O' &&in1[3]=='T') ||( in1[1]==in1[2]==in1[3]=='O' &&in1[0]=='T'))
				
			 
				if(in[j][0]==in[j][1]&& in[j][1]==in[j][2]&& in[j][1]==in[j][3]&& in[j][1]=='O' ||(in[j][0]==in[j][1]&& in[j][1]==in[j][2]&& in[j][2]=='O' &&in[j][3]=='T') ||( in[j][1]==in[j][2]&&in[j][1]==in[j][3]&& in[j][1]=='O' &&in[j][0]=='T'))
				O=true;
			
		}
		
		if(!X && !O)
		{
			for(int j=0;j<4;j++)
			{
				if(in[0][j]=='X'&&in[1][j]=='X'&&in[2][j]=='X'&&in[3][j]=='X' ||( in[0][j]=='X'&&in[1][j]=='X'&&in[2][j]=='X' &&in[3][j]=='T') ||( in[1][j]=='X'&&in[2][j]=='X'&&in[3][j]=='X' &&in[0][j]=='T'))
				X=true;
			else if(in[0][j]=='O'&&in[1][j]=='O'&&in[2][j]=='O'&&in[3][j]=='O'||( in[0][j]=='O'&&in[1][j]=='O'&&in[2][j]=='O' &&in[3][j]=='T') ||( in[1][j]=='O'&&in[2][j]=='O'&&in[3][j]=='O' &&in[j][0]=='T'))
				O=true;

			}
		}	
		if(!X && !O)  //check for diagonal wins
		{
			if(in[0][0]=='X'&&in[1][1]=='X'&&in[2][2]=='X'&&in[3][3]=='X' ||( in[0][0]=='X'&&in[1][1]=='X'&&in[2][2]=='X' &&in[3][3]=='T') ||( in[1][1]=='X'&&in[2][2]=='X'&&in[3][3]=='X' &&in[0][0]=='T'))
				X=true;
			else if(in[0][0]=='O'&&in[1][1]=='O'&&in[2][2]=='O'&&in[3][3]=='O'||( in[0][0]=='O'&&in[1][1]=='O'&&in[2][2]=='O'&&in[3][3]=='T') ||( in[1][1]=='O'&&in[2][2]=='O'&&in[3][3]=='O' &&in[0][0]=='T'))
				O=true;
			else if(in[0][3]=='X'&&in[1][2]=='X'&&in[2][1]=='X'&&in[3][0]=='X' ||( in[0][3]=='X'&&in[1][2]=='X'&&in[2][1]=='X' &&in[3][0]=='T') ||( in[3][1]=='X'&&in[2][1]=='X'&&in[1][2]=='X' &&in[0][3]=='T'))
				X=true;
			else if(in[0][3]=='O'&&in[1][2]=='O'&&in[2][1]=='O'&&in[3][0]=='O'||( in[0][3]=='O'&&in[1][2]=='O'&&in[2][1]=='O'&&in[3][0]=='T') ||( in[3][1]=='O'&&in[2][1]=='O'&&in[1][2]=='O' &&in[0][3]=='T'))
				O=true;
			else 
			{
				for(int u=0;u<4;u++)
				{
					for(int j=0;j<4;j++)
					{
						if(in[u][j]=='.')
						{	
							notfinished=true;
						//	break;

						}
					}
				}
				if(!notfinished)
					draw=true;

			}
		}


		
       if(X)
		   fout<<"Case #"<<i+1<<": X won"<<endl;
	   else if(O)
		   fout<<"Case #"<<i+1<<": O won"<<endl;
	   else if(draw)
		   fout<<"Case #"<<i+1<<": Draw"<<endl;
	   else if(notfinished)
		   fout<<"Case #"<<i+1<<": Game has not completed"<<endl;


	}

	return 0;
}