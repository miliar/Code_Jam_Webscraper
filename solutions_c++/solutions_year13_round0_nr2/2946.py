#include <iostream>
#include <string>
#include <fstream>
#include <sstream> //For the stringstream class.
#include <stdarg.h> //For the indefinite arguments
#include <iomanip>

using namespace std;


struct	instanceType
{
	int*&		operator[](int index)
	{
		return heights[index];
	}
	
	void		allocateMemory(int NN, int MM)
	{
		if(heights)
		{
			for(int cnt=0; cnt<N; cnt++)
				delete[] heights[cnt];
			delete[] heights;
			heights=0;
		}
		
		N=NN;
		M=MM;
		
		heights=new int*[N];
		for(int cnt=0; cnt<N; cnt++)
			heights[cnt]=new int[M];
	}
	
	void	destroy()
	{
		if(heights)
		{
			for(int cnt=0; cnt<N; cnt++)
				delete[] heights[cnt];
			delete[] heights;
			heights=0;
		}
		N=0;
		M=0;
	}
	
	instanceType()
	{
		N=0;
		M=0;
		heights=0;
	}
	
	int			N;
	int			M;
	int**		heights;
};


struct	resultType
{
	resultType(int r)
	{
		result=r;
	}
	
	resultType()
	{
		result=-1;
	}
	
	int		result;
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


//The solver.
resultType	solve(instanceType&	instance)
{
	bool			bad_r(false), bad_c(false);
	int				height(0);
	
	for(int cnt_r=0; cnt_r<instance.N; cnt_r++)
	for(int cnt_c=0; cnt_c<instance.M; cnt_c++)
	{
		bad_r=false;
		bad_c=false;
		height=instance[cnt_r][cnt_c];
		for(int c=0; c<instance.M; c++)
			if(instance[cnt_r][c]>height)	bad_c=true;
		for(int r=0; r<instance.N; r++)
			if(instance[r][cnt_c]>height)	bad_r=true;
		
		if(bad_r && bad_c)	return resultType(0);
	}
	
	return resultType(1);
}


void	readInstace(ifstream& input_file, instanceType&	instance)
{
	int N(0), M(0);
	
	input_file>>N;
	input_file>>M;
	instance.allocateMemory(N,M);
	
	
	
	for(int cnt_r=0; cnt_r<N; cnt_r++)
	for(int cnt_c=0; cnt_c<M; cnt_c++)
		input_file>>instance[cnt_r][cnt_c];
}


void	writeSolution(ofstream& output_file, resultType& solution, int numCase, bool winEOL=false)
{
	output_file<<"Case #"<<numCase<<": ";
	
	switch(solution.result)
	{
		case 0:output_file<<"NO"; break;
		case 1:output_file<<"YES"; break;
	}
	
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







