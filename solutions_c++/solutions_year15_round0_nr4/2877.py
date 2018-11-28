#include <stdint.h>
#include <iostream>

#include <fstream>
#include<boost/math/common_factor.hpp>


using namespace std;



int detLcm(int n){

  int lcm1=1;
  for(int i=1;i<=n;i++ ){
    lcm1=boost::math::lcm(i,lcm1);
  }
  return lcm1;

}


int main(){

   ifstream *infile=new ifstream();
   infile->open("input.txt");

   ofstream myfile;
   myfile.open("output.txt");

  uint16_t test_cases;
  *infile>>test_cases;

  uint16_t tc = test_cases;
  uint16_t x=1;

  cout<<"LCM"<<detLcm(100)<<std::endl;

  while(test_cases>0)
    {
      uint16_t X,R,C,RC=0;
      
      *infile>>X; *infile>>R; *infile>>C;
      RC=R*C;
      if(RC%X!=0){	
	myfile<<"Case #"<<x<<": "<<"RICHARD"<<std::endl;	
	test_cases--;
	x++;
	continue;
      }

      uint32_t tlcm=(uint32_t)detLcm(X);

      if(RC<tlcm)
	myfile<<"Case #"<<x<<": "<<"RICHARD"<<std::endl;
      else{
	uint16_t magic=RC-tlcm;
	if(magic%X==0 )
	   myfile<<"Case #"<<x<<": "<<"GABRIEL"<<std::endl;
	else
	  myfile<<"Case #"<<x<<": "<<"RICHARD"<<std::endl;
      }
      
      //algo: VERY CRYPTIC :(
      /*
      uint16_t i=0;
      for(i=1;i<=X;i++){
	if(RC%i==0){
	  continue;
	}
	else
	  break;
      }

      if(i<=X)
	myfile<<"Case #"<<x<<": "<<"RICHARD"<<std::endl;
      else
	myfile<<"Case #"<<x<<": "<<"GABRIEL"<<std::endl;
      */
      x++;
      test_cases--;
    }

  infile->close();
  myfile.close();

  return 0;
}
