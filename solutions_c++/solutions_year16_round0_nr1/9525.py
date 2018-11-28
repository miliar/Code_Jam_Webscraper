#include <iostream>
#include <vector>
#include <map>

using namespace std;

unsigned int sum(unsigned int *vector)
{
	unsigned int sum = 0;

	for (int i =0; i < 10;i++)
	{
	   sum+=vector[i];
	}

	return sum;
}	


unsigned int calculate_number (unsigned int initial)
{
	map <unsigned int, unsigned int> visited_numbers;
	unsigned int digits [10];
	for (unsigned int i=0; i< 10; i++)
	{
		digits[i] =0;
	}
 
	unsigned int multiple = 1;
	while (sum (&digits[0]) < 10 &&  visited_numbers.find (initial*multiple)== visited_numbers.end()){
	     unsigned int calculation = multiple * initial;
             //cout << "visiting: " << calculation << endl;
             visited_numbers.insert (pair<unsigned int, unsigned int> (calculation, calculation));
	        
	     while (calculation > 0){
	     	unsigned int digit = calculation % 10;
		calculation /= 10;		
	        digits [digit] = 1;
	      }		
	      multiple++;	
	}

        if (sum(&digits[0]) == 10)
	{
	   return (multiple-1) * initial;  	    		
	}
	else
        {	
	   return 0;	
        }
}




int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      unsigned int case_ = 0;
      cin >> case_;
      unsigned int result = calculate_number (case_);
      if (result == 0){
       cout << "Case #"<< i+1 <<":" << " " << "INSOMNIA" << endl;
      }else{	
       cout << "Case #"<< i+1 <<":" << " " << result << endl;	 
      }   
}

   
}
