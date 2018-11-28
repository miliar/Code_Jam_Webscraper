#include<iostream>
#include<string>
#include<cmath>
#include<fstream>
#include<sstream>

using namespace std;

int main()
{
	int counter=0;
	int tcCount, tcNum=0;
	long double rCM, tML, t;
	string* input = NULL;
	
	ifstream inFile("C:\\Dev-Cpp\\Workspace\\GC\\input.in");
	ofstream opFile("C:\\Dev-Cpp\\Workspace\\GC\\output.in");

	if(inFile.is_open() && opFile.is_open())
	{
		inFile>>tcCount;
		tcNum=0;
		
		while(inFile.good() && tcNum<tcCount)
		{
			inFile>>rCM;
			inFile>>tML;
			
			tcNum++;
			counter=0;
			t=pow(rCM+1,2)-pow(rCM,2);
			while(t<=tML)
			{
				counter++;
				tML=tML-t;
				t=t+4;
			}
			opFile<<"Case #"<<tcNum<<": "<<counter<<"\n";
		}
		
		inFile.close();
		opFile.close();
		
	}
	else 
	{
		cout<<"File not found"<<"\n"; 
		inFile.close();
		opFile.close();
	}
}

