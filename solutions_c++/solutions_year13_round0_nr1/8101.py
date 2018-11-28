#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){

	int TC;
	ifstream in("A-small-attempt0.in");
	ofstream o("A-small-attempt0.out");
	in>>TC;
	char board[4][4];

	

	for(int iTmp=1;iTmp<=TC;iTmp++)
	{
		char tmpChar;
			for(int i=0;i<=3;i++)
			{
				for(int j=0;j<=3;j++)
				{
					in>>tmpChar;
					board[i][j]=tmpChar;
					
				}
				
			}

			bool Xflag=false,Oflag=false,Tflag=false,Dflag=false,skip=true;
			std::string tmpStingHor,tmpStingVer;
			bool flag=true;
			for(int i=0;i<=3;i++)
			{
				Xflag=false,Oflag=false;
				tmpStingHor="";
				for(int j=0;j<=3;j++)
				{
					if(board[i][j]=='.')
					{
						flag=false;
						
					}

					tmpStingHor+=board[i][j];

					
				}

				if(tmpStingHor.find("X")!=string::npos && tmpStingHor.length()==4)
				Xflag=true;
				else
				Xflag=false;

				if(tmpStingHor.find("O")!=string::npos && tmpStingHor.length()==4)
				Oflag=true;
				else
				Oflag=false;

				if(tmpStingHor.find(".")!=string::npos)
				Dflag=true;
				else
					Dflag=false;
				
				if(Xflag==true && Oflag==false && Dflag==false)
				{
					skip=false;
					break;
				}

				if(Xflag==false && Oflag==true && Dflag==false)
				{
					skip=false;
					break;
				}

				
			}

			//************
			if(skip==true)
			{

			for(int i=0;i<=3;i++)
			{
				Xflag=false,Oflag=false;
				tmpStingVer="";
				for(int j=0;j<=3;j++)
				{
					if(board[j][i]=='.')
					{
						flag=false;
						break;
					}

					tmpStingVer+=board[j][i];

					
				}
				
				if(tmpStingVer.find("X")!=string::npos && tmpStingVer.length()==4)
				Xflag=true;
				else
					Xflag=false;

				if(tmpStingVer.find("O")!=string::npos && tmpStingVer.length()==4)
				Oflag=true;
				else
					Oflag=false;

				if(tmpStingVer.find(".")!=string::npos)
				Dflag=true;
				else
					Dflag=false;

				
				if(Xflag==true && Oflag==false && Dflag==false)
				{
					break;
				}

				if(Xflag==false && Oflag==true && Dflag==false)
				{
					break;
				}


			}
			}


			if(!((Xflag==false && Oflag==true && Dflag==false) || (Xflag==true && Oflag==false && Dflag==false)))
			{
			Xflag=false,Oflag=false;
			std::string dia1,dia2;
			dia2+=board[0][3]+board[1][2]+board[2][1]+board[3][0];
					
					dia1=board[0][0];
					dia1+=board[1][1];
					dia1+=board[2][2];
					dia1+=board[3][3];
					
					dia2=board[0][3];
					dia2+=board[1][2];
					dia2+=board[2][1];
					dia2+=board[3][0];
					
					

			if(dia1.find("X")!=string::npos && dia1.length()==4)
				Xflag=true;
			else
				Xflag=false;

				if(dia1.find("O")!=string::npos && dia1.length()==4)
				Oflag=true;
				else
					Oflag=false;
				if(dia1.find(".")!=string::npos)
				Dflag=true;
				else
					Dflag=false;
				

			if(!((Xflag==false && Oflag==true && Dflag==false) || (Xflag==true && Oflag==false && Dflag==false)))
			{
			Xflag=false,Oflag=false;
				if(dia2.find("X")!=string::npos && dia2.length()==4)
				Xflag=true;
				else
					Xflag=false;

				if(dia2.find("O")!=string::npos && dia2.length()==4)
				Oflag=true;
				else
					Oflag=false;
				
			}

			}
				
				

				if(Xflag==true && Oflag==false)
				o<<"Case #"<<iTmp<<": "<<"X won"<<endl;

				else
			if(Xflag==false && Oflag==true)
				o<<"Case #"<<iTmp<<": "<<"O won"<<endl;
			else if(flag==true)
				o<<"Case #"<<iTmp<<": "<<"Draw"<<endl;
			else				
				o<<"Case #"<<iTmp<<": "<<"Game has not completed"<<endl;

	}



	system("pause");
	return 0;
}