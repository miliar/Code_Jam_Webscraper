#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

std::string see_if_it_is_a_solution (unsigned int x, unsigned int r, unsigned int c)
{
    if (((r * c) % x) != 0)
    {
	return "RICHARD";
    } 
    
    if (x == 2)
    {
    	return "GABRIEL";
    }
    
    if (x == 4)
    { 
       if (r * c <= 8)
       {
	  return "RICHARD";
       }
       else
       {
	   return "GABRIEL";
       }
    }
    
    double squareside = (int)ceil (sqrt ((double) x));  
    if (squareside > r || squareside > c)
    {
	  return "RICHARD";
    }
    
    return "GABRIEL";
}

int main ()
{
    unsigned int number_of_cases = 0;
    cin >> number_of_cases;
    
    for (int i = 0; i < number_of_cases; i++)
    {
       unsigned int x, r, c;	
       cin >> x >> r >> c;
       std::string winner = see_if_it_is_a_solution (x,r,c);
       cout << "Case #" << i + 1 << ": " << winner << endl;
    } 	
}

