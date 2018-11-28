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
		ans1 = 0;
		ans2 = 0;
		for(int cnt1 = 0; cnt1 < 4; ++cnt1)
		for(int cnt2 = 0; cnt2 < 4; ++cnt2)
		{lines1[cnt1][cnt2]=0; lines2[cnt1][cnt2]=0;}
	}
	
	int	ans1;
	int	ans2;
	int	lines1[4][4];
	int	lines2[4][4];
};


struct	resultType
{
	resultType()
	{
		result = 0;
		card = 0;
	}
	
	int		result;
	int		card;
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
	
	for(int cnt1 = 0; cnt1 < 4; ++cnt1)
	{
		for(int cnt2 = 0; cnt2 < 4; ++cnt2)
		{
			if(instance.lines1[instance.ans1-1][cnt1] == instance.lines2[instance.ans2-1][cnt2])
			{
				solution.result++;
				solution.card = instance.lines1[instance.ans1-1][cnt1];
				break;
			}
		}
	}
	
	return solution;
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	input_file>>instance.ans1;
	for(int cnt1 = 0; cnt1 < 4; ++cnt1)
	for(int cnt2 = 0; cnt2 < 4; ++cnt2)
		input_file>>instance.lines1[cnt1][cnt2];
	input_file>>instance.ans2;
	for(int cnt1 = 0; cnt1 < 4; ++cnt1)
	for(int cnt2 = 0; cnt2 < 4; ++cnt2)
		input_file>>instance.lines2[cnt1][cnt2];
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase)
{
	output_file<<"Case #"<<numCase<<": ";
	
	switch(solution.result)
	{
		case 0:output_file<<"Volunteer cheated!"; break;
		case 1:output_file<<solution.card; break;
		case 2:
		case 3:
		case 4:output_file<<"Bad Magician!"; break;
	}
	
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







