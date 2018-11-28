#include <iostream>
#include <string>
#include <fstream>
using namespace std;
bool Check(int X,int R, int C)
{
	//false means Richard Wins
	//true means Gabrial Wins
	if(X==4)
	{
		if(R==4 && C==4)
			return true;
		else if((R==4 && C==3) || (R==3 && C==4))
			return true;
		else
			return false;
	}
	else if(X==3)
	{
		if(R==3 && C==3)
			return true;
		else if((R==4 && C==3) || (R==3 && C==4))
			return true;
		else if((R==3 && C==2) || (R==2 && C==3))
			return true;
		else
			return false;
	}
	else if(X==2)
	{
		if(R==4 && C==4)
			return true;
		else if(R==2 && C==2)
			return true;
		else if((R==4 && C==3) || (R==3 && C==4))
			return true;
		else if((R==4 && C==2) || (R==2 && C==4))
			return true;
		else if((R==4 && C==1) || (R==1 && C==4))
			return true;
		else if((R==3 && C==2) || (R==2 && C==3))
			return true;
		else if((R==2 && C==1) || (R==1 && C==2))
			return true;
		else
			return false;
	}
	else
	{
		return true;
	}
}
void main()
{
	ifstream in("SmallD.in");
	ofstream out("SmallD_Out.out");
	int testcases;
	in>>testcases;
	for (int i=0;i<testcases;i++)
	{
		int X,R,C;
		in>>X>>R>>C;
		bool var = Check(X,R,C);
		if(var == false)
			out<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
		if(var == true)
			out<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
	}
	in.close();
	out.close();
}