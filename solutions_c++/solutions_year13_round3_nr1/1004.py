#include <iostream>
#include <string>
#include <fstream>
#include <sstream> //For the stringstream class.
#include <stdarg.h> //For the indefinite arguments
#include <iomanip>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>    // std::sort
#include <list>			// std::list

//#include "infiniteprecision.h"


using namespace std;

#define MAX_SIZE	10000

struct	instanceType
{
	void		destroy()
	{
	}
	
	instanceType()
	{
		name="";
		n=0;
	}
	
	string		name;
	long long	n;
};


struct	resultType
{
	~resultType()
	{
	}
	
	resultType()
	{
		n_value=0;
	}
	
	long long n_value;
};


//****************************************


//This function checks if a file exists.
bool file_existence(char* file_name=0)
{
	ifstream file;
	bool existence(false);
	
	file.open(file_name,ios::in);
	existence=file.good();
	file.close();
	
	return existence;
}


//Returns the int representation of the text of a string.
int toInt(const string& text)
{
	int number;
	stringstream value (stringstream::in | stringstream::out);
	//Insert the string with the value in the string-stream interface.
	value<<text;
	//Get the nomber in int format;
	value>>number;
	return number;
}


//Check if a number is a palindrome.
bool is_palindrome(long long number)
{
  long long reversed(0), n(number);

  while (n > 0)
  {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return (number == reversed);
}


bool	is_a_vowel(char	c)
{
	return ((c=='a')||(c=='e')||(c=='i')||(c=='o')||(c=='u'));
}

//The solver.
void	solve2(instanceType&	instance, resultType& solution)
{
	long long*	ns=new long long[10000000];
	long long	length=instance.name.size();
	long long	ini(0),fin(0);
	
	for(long long cnt=0; cnt<10000000; cnt++)	ns[cnt]=-1;
	
	for(long long cnt=0; cnt<length; cnt++)
	{
		ini=-1;
		fin=-1;
		for(long long cnt2=cnt; cnt2<length; cnt2++)
		{
			if(!is_a_vowel((char)instance.name[cnt2]))
			{
				if(ini==-1) ini=cnt2;
				
				fin=cnt2;
				if(fin-ini+1>=instance.n) 
				{
					ns[cnt]=fin;
					break;
				}
			}
			else
			{
				
				ini=-1;
				fin=-1;
			}
		}
	}
	
	solution.n_value=0;
	
	for(long long cnt=0; cnt<length; cnt++)
	{
		if(ns[cnt]!=-1)
		{
			solution.n_value += length-ns[cnt];
		}
	}
	
	delete[] ns;
}


void	solve(instanceType&	instance, resultType& solution)
{
	long long*	inis=new long long[10000000];
	long long*	fins=new long long[10000000];
	long long	length=instance.name.size();
	long long	ini(0), fin(0);
	long long	total=0;
	
	for(long long cnt=0; cnt<10000000; cnt++)	{inis[cnt]=-1; fins[cnt]=-1;}
	
	
	ini=-1;
	fin=-1;
	for(long long cnt=0; cnt<length; cnt++)
	{
		if(!is_a_vowel((char)instance.name[cnt]))
		{
			if(ini==-1) ini=cnt;
		}
		else
		{
			if(ini!=-1)
			{
				fin=cnt-1;
				if(fin-ini+1>=instance.n) 
				{
					inis[total]=ini;
					fins[total]=fin;
					total++;
				}
				ini=-1;
				fin=-1;
			}
		}
	}
	
	if((ini!=-1) && (fin==-1))
	{
		fin=length-1;
		if(fin-ini+1>=instance.n) 
		{
			inis[total]=ini;
			fins[total]=fin;
			total++;
		}
	}
	
	
	long long start(0);
	
	solution.n_value=0;
	
	for(long long cnt=0; cnt<total; cnt++)
	{
		//cout<<inis[cnt]<<"  "<<fins[cnt]<<"\n";
		solution.n_value += (inis[cnt]+1-start)*(length-(inis[cnt]+instance.n-1));
		//for(long long cnt2=0; cnt2<fins[cnt]-(inis[cnt]+instance.n)+1; cnt2++)
			//solution.n_value += (length-(inis[cnt]+instance.n-1))-(cnt2+1);
		solution.n_value += (fins[cnt]-(inis[cnt]+instance.n)+1)*(length-(inis[cnt]+instance.n-1)) - (long long)(((fins[cnt]-(inis[cnt]+instance.n)+1)*(fins[cnt]-(inis[cnt]+instance.n)+2))/2.0);
		start=fins[cnt]-instance.n+2;
	}
	cout<<"\n";
	
	delete[] inis;
	delete[] fins;
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	input_file>>instance.name;
	input_file>>instance.n;
}


void	displayInstance(instanceType&	instance)
{
	//cout<<instance.name<<"  "<<instance.n<<"\n";
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase, bool winEOL=false)
{
	output_file<<"Case #"<<numCase<<":";
	
	output_file<<" "<<solution.n_value;
	
	output_file<<(winEOL ? "\r\n" : "\n");
}


int main(int numArgs, char** args)
{
	//Check if the arguments seem rigth.
	if(numArgs>2)
	{
		printf("The only parameter accepted is the file name.\n");
		return 0;
	}
	
	//VARS
		int				numCases(0);
		instanceType	instance;
		resultType*		solutions(0);
		bool			winEOL(true);
		
		//Files streams and names.
		string input_file_name;
		ifstream input_file;
		string output_file_name;
		ofstream output_file;
	
	
	//Get the inpput files names, depending on the number of arguments sent.
	if(numArgs==1)
	{
		input_file_name="input.txt";
		output_file_name="output.txt";
	}
	else
	{
		input_file_name=args[1];
		output_file_name=input_file_name;
		output_file_name.replace(input_file_name.size()-3,3,"_output.out");
	}
	
	//Check if the input file exists.
	if(file_existence((char*)input_file_name.c_str())==false)
	{
		printf("The input file does not exists.\n");
		return 0;
	}
	
	//Work the input file.
	input_file.open(input_file_name.c_str(),ios::in);
	//Read the number of cases.
	input_file>>numCases;
	
	//Get space for the solutions.
	solutions=new resultType[numCases];
	
	//*********************
	//*********************
	//INPUT
	
	//Solve the instances.
	for(int cnt_cases=0; cnt_cases<numCases; cnt_cases++)
	{
		readInstace(input_file, instance);
		solve(instance, solutions[cnt_cases]);
		displayInstance(instance);
		cout<<"Case: "<<cnt_cases<<"\n";
		
	}
	
	input_file.close();
	
	//*********************
	//*********************
	//OUTPUT
	
	//Write the output file.
	output_file.open(output_file_name.c_str(),ios::out);
	
	for(int cnt_solutions=0; cnt_solutions<numCases; cnt_solutions++)
		writeSolution(output_file, solutions[cnt_solutions], cnt_solutions+1, winEOL);
	
	output_file.close();
	
	//*********************
	//*********************
	
	delete[] solutions;
	solutions=0;
	instance.destroy();
	
	cin.get();
}



