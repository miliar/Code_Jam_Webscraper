#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <fstream>
using namespace std;

ofstream myAns;
ifstream Qfile;

int nextChar(string String, int indexCur)
{
	int Rps=1;
	char charCur=String.c_str()[indexCur];
	int index=indexCur+1;
	while(index<String.length()
		&& charCur==String.c_str()[index])
	{
		index++;
		Rps++;
	}
	return Rps;
}

int checkSame(string *Strings,int lines)
{
	int *charIndex=new int[lines];
	int *Rps=new int[lines];
	char *charComp=new char[lines];

	int moves=0;

	for(int i=0;i<lines;i++)
	{
		charIndex[i]=0;;
	}

	//first run
	char model=Strings[0].c_str()[charIndex[0]];		
	for(int i=1;i<lines;i++)
	{		
		if(Strings[i].c_str()[charIndex[i]]!=model)
		{
			return -1;
		}
	}

	while(model!=0)
	{
		//how many repeat to next
		for(int i=0;i<lines;i++)
		{
			Rps[i]=nextChar(Strings[i], charIndex[i]);
		}

		//nextChar
		for(int i=0;i<lines;i++) charIndex[i]+=Rps[i];	
		for(int i=0;i<lines;i++) charComp[i]=Strings[i].c_str()[charIndex[i]];

		//is next possible
		model=charComp[0];
		for(int i=1;i<lines;i++)
		{		
			if(Strings[i].c_str()[charIndex[i]]!=model)
			{
				return -1;
			}
		}

		//how minMove is
		int meanRps=0;
		for(int i=0;i<lines;i++) meanRps+=Rps[i];
		meanRps/=lines;
		for(int i=0;i<lines;i++) moves+= abs(Rps[i]-meanRps);

	}

	return moves;

	delete []charIndex;
	delete []Rps;
	delete []charComp;
}

void Solve(int caseNum)
{
	int lines;
	Qfile>>lines;

 	string *Strings=new string[lines];
	
	for(int i=0;i<lines;i++)
	{
		Qfile>>Strings[i];
	}

 	int minMove=checkSame(Strings,lines);
	
	myAns<<"Case #"<< caseNum <<": ";
	if(minMove!=-1)
		myAns<<minMove;
	else
		myAns<<"Fegla Won";

	myAns<<endl;


	delete []Strings;
}


int main(int argc, char *argv[])
{
	int T=0;
	int i=0;

	Qfile.open("A-small-attempt0.in");
	myAns.open ("MyAnser.txt");
		
	Qfile>>T;
	
	
	for(i=0; i<T; i++)	
	{						
		Solve(i+1);
	}
	myAns.close();
	Qfile.close();
    
	system("PAUSE");
    return EXIT_SUCCESS;
}
