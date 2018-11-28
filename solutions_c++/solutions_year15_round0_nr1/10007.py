#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char** arv){
    int testCases=0;
    // shyness array holds all shyness levels
	string shyness;
    int numOfAudience=0;
    int numNecessary=0;
    int maxShyness=0;
    ifstream ifile("input.txt");
    ofstream ofile("output.txt");
    stringstream ss;
    ifile >> testCases;
    for(int x=0;x<testCases;x++){
        ifile >> maxShyness;
		ifile >> shyness;

        for(int y=0;y<maxShyness+1;y++){
            // if shyness index is greater than number in the audience, add until
            // shyness is matched
            if(y>numOfAudience&&shyness[y]!='0'){
                // find number of people to to meet shyness
	
                numNecessary+=y-numOfAudience;
          
                // add those people to the number in the audience and continue
				ss << shyness[y];
				int temp=0;
				ss >> temp;
                numOfAudience+=numNecessary+temp;
            }
            // if shyness index is met or surpassed, we add those people to audience
            else{
				ss << shyness[y];
				int temp=0; 
				ss >> temp;
                numOfAudience+=temp;
            }
			ss.clear();
        }

		ofile << "Case #" << x + 1 << ": " << numNecessary << endl;
        numNecessary=0;
        numOfAudience=0;
    }










}
