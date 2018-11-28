#include <iostream>
#include <fstream>
#include <string>
#include <sstream> 
#include <stdlib.h> 

using namespace std; 

int  main(){
  ifstream myfile;
  ofstream ofile;
  string word;

  myfile.open ("A-small-attempt2.in");
  ofile.open("A-small-attempt2.out");
  getline(myfile, word); 
  int count = 1;
  const char* nbcases= word.c_str();
  int cases = atoi(nbcases);
  while (count<=cases){
 
    ofile << "Case #"  << count << ": ";
    getline(myfile,word);
    int maxS = word[0]-'0';
    int standing = 0;
    int result = 0;
    for(size_t s = 2; s<word.length(); s++){
       int diff = 0;
      if(word[s]!=0 && standing < s-2)
	diff = s-2-standing;
      result+=diff;
      standing+=word[s]-'0'+diff;
    }
    ofile << result << endl;
    count++;
  }
  ofile.close();
  myfile.close();
  return 0;
}
