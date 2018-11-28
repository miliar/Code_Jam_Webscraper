// tiktak.cpp : Defines the entrO point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
ifstream input; 

int _tmain(int argc, _TCHAR* argv[])
{
	
	ofstream output;
	output.open("answer.txt",ios::out);
	int couter;
	input.open("datain.txt",ios::in);
	input>>couter;
	char x[4][4];
	string temp=",";
	char temp2;
	string temp3;
	for (int v = 1; v <= couter; v++)
	{
		temp=",";
	for (int j = 0; j < 4; j++)
		{

			for (int k = 0; k < 4; k++)
			{
				input>>x[j][k];
				

			}
		}
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
				temp3=x[i][j];
				temp.append(temp3);
		}
		temp.append(",");
		for (int k = 0; k < 4; k++)
		{
			temp3=x[k][i];
			temp.append(temp3);
		}
		temp.append(",");
	}
	
	for (int i = 0; i < 4; i++)
	{
		temp3=x[i][i];
		temp.append(temp3);
	}
	temp.append(",");
	for (int i = 0; i < 4; i++)
	{
		temp3=x[i][3-i];
		temp.append(temp3);
	}
		  
		if (temp.find("XXXX")!=-1||temp.find("TXXX")!=-1||temp.find("XTXX")!=-1||temp.find("XXTX")!=-1||temp.find("XXXT")!=-1)
		  {
			  output<<"Case #"<<v<<": X won"<<endl;
		  }
		  else if (temp.find("OOOO")!=-1||temp.find("TOOO")!=-1||temp.find("OTOO")!=-1||temp.find("OOTO")!=-1||temp.find("OOOT")!=-1)
		  {
			  output<<"Case #"<<v<<": O won"<<endl;
		  }
		  else if (temp.find(".")!=-1)
		  {
			  output<<"Case #"<<v<<": Game has not completed"<<endl;
		  }
		  else
		  {
			  output<<"Case #"<<v<<": Draw"<<endl;
		  }
	}
	return 0;
}
