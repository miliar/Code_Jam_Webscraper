#include <iostream>
#include <string>
#include <stdlib.h> 
#include <fstream>
using namespace std;

int solveCase(string line){
	int * tab ;
	tab = new int[line.length()-2];
	int maxS = line[0] - '0';
	for(int i=2;i < line.length(); i++){
		tab[i-2] =  line[i] - '0';
	}
	int currentStanding = tab[0];
	int toAdd=0;
	for(int j=1; j<line.length()-2; j++){
		int gap = currentStanding-j;
		if(gap<0){
			toAdd = toAdd + abs(gap);
			currentStanding= currentStanding + abs(gap);			
		}
		currentStanding= currentStanding+ tab[j];
	}
	return toAdd;
}
int main(){
	string line;
  ifstream myfile ("input.in");
   ofstream outputFile ("output.txt");
   if(outputFile.is_open()){
  if (myfile.is_open())
  {
	bool  isFirstLine= true;
	  int step=1;
    while ( getline (myfile,line) )
    {
    
	  if(!isFirstLine){
		outputFile << "Case #";
		outputFile << step;
		outputFile << ": ";
		outputFile << solveCase(line);	
		outputFile << endl;
		step++;
	  }
	    isFirstLine= false;
    }
    myfile.close();
	outputFile.close();
  }
   }

  else cout << "Unable to open file"; 

  return 0;
}
