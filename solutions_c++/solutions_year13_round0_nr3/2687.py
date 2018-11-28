#include <iostream>
#include <string>
#include <fstream>
#include <sstream> //For the stringstream class.
#include <stdarg.h> //For the indefinite arguments
#include <iomanip>
#include <cmath>

using namespace std;


struct	instanceType
{
	
	void		destroy()
	{
	}
	
	instanceType()
	{
		A=0;
		B=0;
	}
	
	long long			A;
	long long			B;
};


struct	resultType
{
	resultType(long long r)
	{
		result=r;
	}
	
	resultType()
	{
		result=-1;
	}
	
	long long		result;
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


//The solver.
resultType	solve(instanceType&	instance)
{
	resultType		solution(0);
	long long		lower_aux((long long)ceil((long double)sqrt((long double)instance.A)));
	long long		upper_aux((long long)sqrt((long double)instance.B));
	
	for(register long long cnt_sqrt=lower_aux; cnt_sqrt<=upper_aux; cnt_sqrt++)
	{
		if((is_palindrome(cnt_sqrt))&&(is_palindrome((long long)(cnt_sqrt*cnt_sqrt))))
		{
			solution.result++;
			cout<<"\n"<<cnt_sqrt<<"^2 = "<<(long long)(cnt_sqrt*cnt_sqrt);
		}
	}
	
	
	return solution;
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	input_file>>instance.A;
	input_file>>instance.B;
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase, bool winEOL=false)
{
	output_file<<"Case #"<<numCase<<": ";
	
	output_file<<solution.result;
	
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
		solutions[cnt_cases]=solve(instance);
		
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
	
	//cin.get();
}







