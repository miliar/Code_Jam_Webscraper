#include <sstream>
#include <fstream>
#include <iostream>
#include <string>

#include <cmath>

unsigned long min;
unsigned long max;
int result;

void ReadData(std::ifstream& inputFile)
{
	std::string line;	
	getline(inputFile,line);
	std::stringstream ss;
	ss<<line;
	ss>>min>>max;
}

void Output(int idx)
{
	std::cout<<"Case #"<<idx<<": "<<result<<std::endl;
}

bool is_palindromes(unsigned long idx)
{
	std::stringstream ss;
	ss<<idx;
	std::string line;
	ss>>line;
	for(int j=0; j<line.length()/2; j++){
		if(line[j]!=line[line.length()-j-1]) return false;
	}
	return true;
}

int Judge()
{
	int result=0;
	double droot=std::ceil(std::sqrt(min));
	unsigned long i_min = (unsigned long)droot;
	
	for(unsigned long idx = i_min*i_min; idx<=max; idx += 2*i_min+1, i_min++)
	{
		if(is_palindromes(idx) && is_palindromes(i_min)){	
		     //std::cout<<idx<<" "<<i_min<<std::endl;
			 result++;
		}
		
		
	}
	return result;
}



int main(int argv, char** argc)
{
	std::ifstream inputFile(argc[1]);
	std::string strNumOfCases;
	int n_of_cases=0;
    if(inputFile.is_open()){
    	getline(inputFile, strNumOfCases); 
		std::stringstream ss;
		ss<<strNumOfCases;
		ss>>n_of_cases;
		for(int i=1; i<=n_of_cases; i++){
			ReadData(inputFile);
			result = Judge();
			Output(i);	
			
		}
	}
}
