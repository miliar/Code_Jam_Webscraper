#include <iostream>
#include <fstream>
using namespace std;

bool checkWinG(int X, int R, int C);

int main()
{
	int T,X,R,C;
	bool winG;
	ifstream read;
	ofstream write;
	read.open("D-small-attempt2.txt");
	write.open("ProbDsmallOutput2.txt");

	read>>T;
	for(int i=0; i<T; i++)
	{
		read>>X>>R>>C;
		winG = checkWinG(X,R,C);
		write<<"Case #"<<i+1<<": ";
		if(winG)
			write<<"GABRIEL"<<endl;
		else write<<"RICHARD"<<endl;
	}
	return 0;
}

bool checkWinG(int X, int R, int C)
{
	if(X==1) return true;
	else if(X>R && X>C)
		return false;
	else if(X==2)
	{
		if(((R*C)%2)==0)
			return true;
		else return false;
	}
	else if(X==3)
	{
		if((((R*C)%3)==0) && ((R!=1) && (C!=1)))
			return true;
		else return false;
	}
	else if(X==4)
	{
		if((R<3) || (C<3))
			return false;
		else return true;
	}	
}