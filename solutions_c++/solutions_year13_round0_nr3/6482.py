#include<iostream>
#include<fstream>
#include<malloc.h>

using namespace std;

int palindrome(int number);
int perfectsquare(int lower_limit,int upper_limit);

int main()
{
	char *ifilename = "c:\\C-small-attempt0.in";
    char *ofilename = "c:\\smalloutput.txt";
	int count_testcases, lower_limit,upper_limit,i;
	int fair_and_square_numbers;

	ifstream inputfile(ifilename);
    ofstream outputfile(ofilename);

	if(!inputfile)
     {
       cout << "There is problem in opening file" << ifilename << endl;
       return (0);
     }
    cout << "opened" << ifilename << "for reading" << endl;
   
    inputfile >> count_testcases;

	for(i=0;i<count_testcases;i++)
	{
		inputfile >> lower_limit;
		inputfile >> upper_limit;

		fair_and_square_numbers = perfectsquare(lower_limit,upper_limit);
		 outputfile << "Case #" << i+1 << ":"<< " " << fair_and_square_numbers << "\n" << endl;
	}

	return(0);
   
}


int palindrome(int number)
{
	int n2,n3=0,i;
	
	  n2=number;
      do
       {
          i = number%10;
          number = number/10;
          n3 = n3*10+i;
       }
     while(number>0);
     if(n3==n2 || n2 < 10)
       {
            return(1);
       }
     else
       {
               return(0);
       }
	
}

int perfectsquare(int lower_limit,int upper_limit)
{
	int high,low,mid,square,flag, total_count = 0,i;
	int number,flag_palindrome;
	for(number = lower_limit; number <= upper_limit; number++)
	  {
		  flag_palindrome =  palindrome(number);
		  if(number == 1)
			  total_count++;
		  if(flag_palindrome == 1)
		  {
              high = number/2; 
              low = 0; 
              while(high>=low) 
               { 
                 mid = (low + high)/2; 
                 square = mid * mid; 
                 if(square==number) 
                   { 
					   flag = palindrome(mid);
					   if(flag == 1)
						   total_count++;
                   } 
                 if(square > number) 
                   { 
                     high = mid-1; 
                   } 
                 else 
                   { 
                     low = mid+1; 
                   } 
               } //while ends
		  }//if ends
	  }//for ends
	
	return(total_count);
}

