#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>
#include <fstream>

int main(int argv, char** argc){

  if(argv < 2){
    std::cerr << "Bad input arguments"  << std::endl;
    exit(-1);
  }

  unsigned int T;
  unsigned int Smax;

  unsigned int friends2Invite;
  unsigned int peopleInFavor;
  unsigned int diff;
  unsigned int peopleWithShyLevel;

  std::string shyLevelsStr;
  
  std::ifstream inputFile(argc[1]);
  std::ofstream outputFile("outputFile.txt");
  
  inputFile >> T;

  for(unsigned int i=0; i<T; i++){

    /// Read input line and pass to a string
    inputFile >> Smax >> shyLevelsStr;
    friends2Invite = 0;
    peopleInFavor = (unsigned int)(shyLevelsStr[0] - '0');

    for(unsigned int shyLevel = 1; shyLevel < shyLevelsStr.size(); shyLevel++){
      peopleWithShyLevel = (unsigned int)(shyLevelsStr[shyLevel] - '0') ;

      for(unsigned int p = 1; p <= peopleWithShyLevel; p++){
        if( peopleInFavor < shyLevel ){
          diff = shyLevel - peopleInFavor;
          peopleInFavor += diff ;
          friends2Invite += diff;
        }
        peopleInFavor++;
      }
    }

    outputFile << "Case #" 
               << i+1
               << ": " 
               << friends2Invite 
               << std::endl;
  }


  return 0;
}
