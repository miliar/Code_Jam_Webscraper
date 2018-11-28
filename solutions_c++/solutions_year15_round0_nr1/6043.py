#include <string.h>
#include <stdint.h>
#include <iostream>

#include <fstream>

using namespace std;


int main(){

   ifstream *infile=new ifstream();
   infile->open("input.txt");

   ofstream myfile;
   myfile.open("output.txt");

  uint16_t test_cases;
  *infile>>test_cases;

  uint16_t tc = test_cases;
  uint16_t x=1;

  while(test_cases>0)
    {
      uint16_t N=0,paidAudience=0;
      *infile>>N;

      std::string st;

      *infile>>st;
      uint16_t tot=0;
      
      
      for(uint16_t i=0;i<N;i++){
	
	  tot=tot+(st[i]-'0');	  

	  if((i+1)>tot){
	    uint16_t req=i+1-tot;
	    tot=tot+req;
	    paidAudience=paidAudience+req;
	  }
	  else
	    continue;
      }
      
      myfile<<"Case #"<<x<<": "<<paidAudience<<std::endl;
      x++;
      test_cases--;
    }

  infile->close();
  myfile.close();

  return 0;
}
