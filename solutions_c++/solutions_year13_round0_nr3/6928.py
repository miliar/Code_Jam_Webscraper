#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main() {
  int T;     //Number of test cases 
  int A, B;  //limits of numbers
  int rev_isqrrt; //Reverse of number
  int fair_sqr; //Number of fair squres

  
  //Variables for checking palindromes
  int digit; //Digit of numbers
  int num; //Number
  int rev_num; // reverse of loop counter
  
  int isqrrt_num; //Integer part of root of number
  double dsqrrt_num; //square root of number
  
  ifstream myifile( "C:\\Users\\Mukul\\workspace\\fair_square\\src\\C-small-attempt2.in" );
  string line;
  
  ofstream myofile;
  myofile.open ("fair_square.txt");
  
  if (myifile){
	  getline(myifile, line);
	  istringstream iss(line);
	  iss>>T;
	  
  }
  
  for(int case_count = 1; case_count<= T; case_count++){
	      fair_sqr =0;
	      if (myifile){
	     	  getline(myifile, line);
	     	  istringstream iss(line);
	     	  iss>>A;
	     	  iss>>B;
	      }
		    
		  for(int lc = A; lc <= B; lc++){
			  rev_isqrrt = 0;
			  rev_num = 0;
			  dsqrrt_num = sqrt(lc);
		  	  isqrrt_num = dsqrrt_num;
			  
			  if (isqrrt_num == dsqrrt_num){
				  
				  do
				  {	  digit =  isqrrt_num%10;
					  
					  rev_isqrrt = (rev_isqrrt*10) + digit;
					 
				  	  isqrrt_num = isqrrt_num/10;
				  }while (isqrrt_num!=0);
				  num = lc;
				  do
			  		  {	  digit =  num%10;
			  			  
			  			  rev_num = (rev_num*10) + digit;
			  			  
			  		  	  num = num/10;
			  		  }while (num!=0);
				  
				  
				  if ((dsqrrt_num == rev_isqrrt) && (lc == rev_num)){
					  	fair_sqr++;
				  		
				  }
				  
			  }
			   
			  
		  	}
		  myofile<<"Case #" <<case_count<<": "<<fair_sqr<<"\n";
		  
  }
  myofile.close();
  myifile.close();
  return 0;
}