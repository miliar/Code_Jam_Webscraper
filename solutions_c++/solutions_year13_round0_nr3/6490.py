#include <iostream>  
#include <fstream>    
#include <stdlib.h>   
#include <string>    
using namespace std;  
#include <list>
#include <sstream>;

bool isPalindrome(string);
 
int main()
{
  ifstream in ("C-small-attempt0.in");        
  ofstream out("A-large-practice.out");       
  if (!in.is_open() || in.eof() )               
  {
    cerr << "ERROR: invalid input file" << endl;
    return (-1);
  }
  if(!out.is_open())                           
  {
    cerr << "ERROR: couldn't create ouput file" << endl;
    return (-1);
  }
 
  int numCases;                      
  string endpointA;
  string endpointB;
  int count;
  int lowerbound;
  int upperbound;

  std::string line;
                         
  getline( in, line, '\n' );           
  numCases = atoi( line.c_str() );     
 
  for (int c=1; c<=numCases; c++)               
  {
	// clear 
	count = 0;
	endpointA = "";
	endpointB = "";
	lowerbound = 0;
	upperbound = 0;

	getline( in, line); 
	endpointA = line.substr(0, line.find(" "));
	endpointB = line.substr(line.find(" ") + 1);
	
	lowerbound = atoi( endpointA.c_str() );
	upperbound = atoi( endpointB.c_str() );

	for (int i = lowerbound; i <= upperbound; i++)
	{
		stringstream ss;
		ss << i;
		string str = ss.str();

		// check if palindrome
		if (isPalindrome(str) == true)
		{
		// if palindrome sqrt
		   int j;
		   for (j = 1; j <= i; j++)
		   {
			  if ( ((i % j) == 0) && ( (j * j) == i) )
			  {
				// check if result is palindrome
				stringstream ss;
				ss << j;
				string str = ss.str();
				if (isPalindrome(str) == true)
				{
					// if yes then increment count and continue
					count++;
				}
			    // if result is not palindrome then continue
			  }
		   
		   }
		}

		// if palindrome is not sqrt then continue

	// if not palindrome then continue

		
	}
	out << "Case #" << c << ": " << count << endl;
  }
  in.close();       
  out.close();      
 
  return 0;
}

bool isPalindrome(string a)
{
	bool status = false;
	string reverse = "";
	for (int i = a.size() - 1; i >= 0; i--)
	{
		reverse.append(1, a[i]);	
	}
	if ( (a.find(reverse) == 0) && (reverse.find(a) == 0) )
		status = true;

	return status;
}