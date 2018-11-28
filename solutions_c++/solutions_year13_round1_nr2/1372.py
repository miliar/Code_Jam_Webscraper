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

using namespace std;

#define MAX_BYTES 100

struct			UBigNumbers
{

	UBigNumbers&		operator+(unsigned char d)
	{
		for(register unsigned char cnt=0; cnt<d; cnt++)
			++(*this);
		return *this;
	}

	UBigNumbers&		operator-(unsigned char d)
	{
		for(register unsigned char cnt=0; cnt<d; cnt++)
			--(*this);
		return *this;
	}

	//++x
	UBigNumbers&		operator++()
	{
		for(register int cnt=0; cnt<MAX_BYTES; cnt++)
		{
			if(mBytes[MAX_BYTES-cnt-1]==255) mBytes[MAX_BYTES-cnt-1]=0;
			else 
			{
				mBytes[MAX_BYTES-cnt-1]++;
				return *this;
			}
		}

		return *this;
	}


	//--x
	UBigNumbers&		operator--()
	{
		for(register int cnt=0; cnt<MAX_BYTES; cnt++)
		{
			if(mBytes[MAX_BYTES-cnt-1]==0) mBytes[MAX_BYTES-cnt-1]=255;
			else 
			{
				mBytes[MAX_BYTES-cnt-1]--;
				return *this;
			}
		}

		return *this;
	}


	//x++
	UBigNumbers		operator++(int)
	{
		UBigNumbers cResult(*this);
 
		++(*this);
		return cResult;
	}

	//x--
	UBigNumbers		operator--(int)
	{
		UBigNumbers cResult(*this);
 
		--(*this);
		return cResult;
	}

	
	UBigNumbers&		operator=(const UBigNumbers& BN)
	{
		for(register int cnt=0; cnt<MAX_BYTES; cnt++)
			mBytes[cnt]=BN.mBytes[cnt];

		return *this;
	}
	
	UBigNumbers()
	{
		for(register int cnt=0; cnt<MAX_BYTES; cnt++)
			mBytes[cnt]=0;
	}
	
	unsigned char		mBytes[MAX_BYTES];
};


#define MAX_SIZE 100000
struct	instanceType
{
	
	void	destroy()
	{
	}

	instanceType()
	{
		E=0;
		R=0;
		N=0;
		for(register int cnt=0; cnt<MAX_SIZE; cnt++)
			v[cnt]=0;
	}
	
	long long	E;
	long long	R;
	long long	N;
	long long	v[MAX_SIZE];
};


struct	resultType
{
	resultType()
	{
		total_gain=0;
	}
	
	long long		total_gain;
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


//Get the integer values from the stream in the different arguments.
void getIntVars(stringstream& values, int num, ...) 
{
	va_list list;
	int* arg;
	
	va_start(list, num);

	for(register unsigned int cnt=0; cnt<num; cnt++)
	{
		arg = va_arg(list, int*);
		values>>*arg;
	}

	va_end(list);
}

//Get th double values from the stream in the different arguments.
void getDoubleVars(stringstream& values, int num, ...) 
{
	va_list list;
	double* arg;
	
	va_start(list, num);

	for(register unsigned int cnt=0; cnt<num; cnt++)
	{
		arg = va_arg(list, double*);
		values>>*arg;
	}

	va_end(list);
}


//Get the integer values from the stream in the array.
void getIntArr(stringstream& values, int num, int* arr)
{
	for(register unsigned int cnt=0; cnt<num; cnt++)
		values>>arr[cnt];
}

//Get the double values from the stream in the array.
void getDoubleArr(stringstream& values, int num, double* arr)
{
	for(register unsigned int cnt=0; cnt<num; cnt++)
		values>>arr[cnt];
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



long long maximum=0;

void	get_maximum(instanceType& instance, long long E, int i, long long gain)
{
	if(i==instance.N)
	{
		if(gain>maximum) maximum=gain;
		return;
	}

	for(register int cnt=0; cnt<=E; cnt++)
	{
		get_maximum(instance, (E-cnt+instance.R>= instance.E ? instance.E : E-cnt+instance.R ), i+1, gain + instance.v[i]*cnt);
	}
}


//The solver.
void	solve(instanceType&	instance, resultType& solution)
{
	long long	energy(instance.E);

	get_maximum(instance, instance.E, 0, 0);
	
	solution.total_gain=maximum;
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	input_file>>instance.E;
	input_file>>instance.R;
	input_file>>instance.N;
	for(register int cnt=0; cnt<instance.N; cnt++)
		input_file>>instance.v[cnt];
}


void	displayInstance(instanceType&	instance)
{
	cout<<instance.E<<"  "<<instance.R<<"  "<<instance.N<<"\n";
	for(register int cnt=0; cnt<instance.N; cnt++)
		cout<<instance.v[cnt]<<"  ";
	cout<<"\n\n";
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase, bool winEOL=false)
{
	output_file<<"Case #"<<numCase<<":";
	
	output_file<<" "<<solution.total_gain;
	
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
		maximum=0;
		solve(instance, solutions[cnt_cases]);
		//displayInstance(instance);
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

