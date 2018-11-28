#include <iostream>
#include <string>
#include <fstream>
#include <sstream> //For the stringstream class.
#include <stdarg.h> //For the indefinite arguments
#include <iomanip>

using namespace std;


struct	instanceType
{
	instanceType()
	{
		C=0.0; F=0.0; X=0.0;
	}
	
	double	C;
	double	F;
	double	X;
};


struct	resultType
{
	resultType()
	{
		result = 0.0;
	}
	
	double	result;
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


//The solver.
resultType	solve(instanceType&	instance)
{
	resultType	solution;
	double		rate(2.0);
	
	
	while(instance.X/rate > instance.C/rate + instance.X/(rate+instance.F))
	{
		solution.result += instance.C/rate;
		rate += instance.F;
	}
	solution.result += instance.X/rate;
	
	return solution;
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	input_file>>instance.C;
	input_file>>instance.F;
	input_file>>instance.X;
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase)
{
	output_file<<"Case #"<<numCase<<": ";
	output_file<<std::fixed<<std::setprecision(7)<<solution.result;
	output_file<<"\r\n";
}


int main(int numArgs, char** args)
{
	//VARS
	int				numCases(0);
	instanceType	instance;
	resultType*		solutions(0);
	
	//Files streams and names.
	string			input_file_name;
	ifstream		input_file;
	string			output_file_name;
	ofstream		output_file;
	
	
	//Get the inpput files names, depending on the number of arguments sent.
	if(numArgs == 1)
	{
		input_file_name = "input.txt";
		output_file_name = "output.txt";
	}
	else
	{
		input_file_name = args[1];
		output_file_name = input_file_name;
		output_file_name.replace(input_file_name.size()-3, 3, "_output.txt");
	}
	
	//Check if the input file exists.
	if(file_existence((char*)input_file_name.c_str())==false)
	{
		printf("The input file does not exists.\n");
		return 0;
	}
	
	//Work the input file.
	input_file.open(input_file_name.c_str(), ios::in);
	//Read the number of cases.
	input_file>>numCases;
	//Get space for the solutions.
	solutions=new resultType[numCases];
	
	//*********************
	//*********************
	//INPUT
	
	//Solve the instances.
	for(int cnt_cases = 0; cnt_cases < numCases; ++cnt_cases)
	{
		readInstace(input_file, instance);
		solutions[cnt_cases] = solve(instance);
	}
	
	input_file.close();
	
	//*********************
	//*********************
	//OUTPUT
	
	//Write the output file.
	output_file.open(output_file_name.c_str(), ios::out);
	
	for(int cnt_solutions = 0; cnt_solutions < numCases; ++cnt_solutions)
		writeSolution(output_file, solutions[cnt_solutions], cnt_solutions+1);
	
	output_file.close();
	
	//*********************
	//*********************
	
	delete[] solutions;
	solutions=0;
	
	//cin.get();
}







