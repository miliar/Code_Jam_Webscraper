#include <sstream>
#include <fstream>
#include <iostream>
#include <string>

int** matrix;
int l;
int w;
bool result; //0 draw, 1 X win, 2 Y win, 3 incomplete

void ReadData(std::ifstream& inputFile)
{
	std::string line;	
	getline(inputFile,line);
	std::stringstream ss;
	ss<<line;

	ss>>l>>w;
	if(l<=0 || w<=0) return;
	
		
	matrix=new int*[l];
	for(int i=0; i<l; i++) matrix[i]=new int[w];

	if(inputFile.is_open()){
		for(int i=0; i<l; ++i){
    		getline(inputFile,line); 
			std::stringstream ss_1;
			ss_1<<line;
			for(int j=0; j<w; ++j){
				ss_1>>matrix[i][j];
			}
		}
//		getline(inputFile,line); 
	}
}

void Output(int idx)
{
	if(result){
		std::cout<<"Case #"<<idx<<": YES"<<std::endl;
	}	
	else{
		std::cout<<"Case #"<<idx<<": NO"<<std::endl;
	}
}

bool Judge()
{
	for(int i=0; i<l; i++){//Vertical check
		int max=matrix[i][0];
		for(int j=1; j<w; j++){
			if(matrix[i][j]>max){
				max=matrix[i][j];
			}
		}
		for(int j=0; j<w; j++){
			if(matrix[i][j]<max){
				for(int m=0; m<l; m++){
					if(matrix[i][j]<matrix[m][j]) return false;
				}
			}
		}
	}
	return true;
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
	for(int i=0; i<l; i++){
		delete[] matrix[i];
	}
	delete[] matrix;
}
