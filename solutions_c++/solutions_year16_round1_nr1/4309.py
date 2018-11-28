#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <ctime>
#include <list>
#include <map>
using namespace std;
#include <conio.h>

map<int, int> MyMap;
list<string> test;
int arr1[32][500];
int arr2[100];
string arr3[1000];
string in1;

ifstream infile;
string STRING;
ofstream offile;
string pattern;

void getop(string & out);

long  main()
{
	infile.open ("c:\\temp\\in.txt");
	offile.open("c:\\temp\\out3.txt");

	int testcases;
	infile >> testcases;
	
	for(int i=1;i<=testcases;i++)
	{	
		int size=0;
		
		infile >> in1;
		//infile >> in2;

		string op;
		getop(op);

			
		cout<<"Case #"<<i<<": "<<op<<endl;
		offile <<"Case #"<<i<<": "<<op<<"\n";
		cout<<endl;
				
	}
	
	getch();
	infile.close(); 
	offile.close();
	return 0;
}

void getop(string & out)
{
	int size=in1.size();
	int max=0;
	int ind=0;
	char init=in1[0];
	int ini=init;
	string str=in1.substr(0,1);
	for(int i=1;i<size;i++)
	{
		int test = in1[i];
		if(test >= str[0])
		{
			str= in1[i] + str;
		}
		else
			str = str + in1[i];
	}
	
	out=str;

}