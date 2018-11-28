// Marwan Alani
// CodeJam 2015

#include <iostream>
#include <fstream>
#include <string>

void processCase(std::ifstream& input,std::ofstream& output,int caseNo) {
   int standing,friends;
   std::string line;
   std::getline(input,line);
   friends = 0;
   standing = 0;
   line = line.erase(0,2);
   for (int i=0; i<line.size(); i++) {
      if (standing < i+1) {
         friends += i - standing;
         standing += i- standing;
      }
      standing += (line[i] - 48);
   }
   //std::cout << "Case #" << caseNo << ": " << friends << std::endl;
   output << "Case #" << caseNo << ": " << friends << std::endl;
}

int main(int argc,char* args[]) {
   if (argc == 2) {
      std::ifstream inputFile;
      std::ofstream outputFile;
      inputFile.open(args[1]);
      outputFile.open("marwan_alani_codejam.out");
      int cases;
      inputFile >> cases;
      inputFile.get();
      for (int i=0; i<cases; i++)
         processCase(inputFile,outputFile,i+1);
      inputFile.close();
      outputFile.close();
   }
   return 0;
}
