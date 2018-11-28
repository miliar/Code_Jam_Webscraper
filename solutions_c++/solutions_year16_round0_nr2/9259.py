#include<iostream>
#include<string>
#include<stdlib.h>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<ostream>
#include<sstream>
using namespace std;
int str_to_int(string strip)
{
	int num=0,c,dec=1;
	c = strip.length()-1;
	//cout << strip.at(strip.length()-1) << endl;
	while(c != -1)
	{
		num+=dec*(strip.at(c)-48);
		c--;
		dec*=10;
	}
	return num;	
}
int main()
{
	int test,k=0;
	string line;
	ifstream my_file("B-large.in");
	ofstream my_file_2("output.in");
	ostringstream oss;
	if(my_file.is_open())
	{
		getline(my_file,line);
		test = str_to_int(line);
	}
	while(getline(my_file,line))
	{	
		k++;
		string strand;
		strand = line ; 
		int i = strand.length()-1;
		while( i > -1)
		{
			if(strand.at(i)=='+')
			{	
				strand.erase(i,1);
				i--;
			}
			else
			{
				break;
			}	
		}	
		while(i>0)
		{
			if(strand.at(i)==strand.at(i-1))
			{
				strand.erase(i,1);
				i--;	
			}
			else
			{
				i--;
			}		
		}
		if(my_file_2.is_open())
		{
			oss << "Case #" << k << ": " << strand.length()<<endl ;
		}		
	}
	my_file_2 << oss.str();
	my_file_2.close();	
	my_file.close();
	return 0;					
}
