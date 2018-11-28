//
//  Google Code Jam - 2013
//  Problem: Fair and Square
//  problemC.cpp
//  Created by Fielding Johnston on 4/13/13.

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <algorithm>

bool isPalindrome( int number );
bool isFairAndSquare( int number );

int main(int argc, const char * argv[])
{
  int n_test_cases;

  // input
  
  scanf("%d", &n_test_cases);
  
  //std::cout<<"Input"<<std::endl<<std::endl;
  //std::cout<<"Test cases: "<< n_test_cases<<std::endl<<std::endl;
  
  // creata  2d array for storing each test case an array of 2 integers (lower bound and upper bound)
  int data[n_test_cases][2];
  
  for ( int test_case = 0; test_case < n_test_cases; test_case++ )
  {
    //std::cout<<"Case #"<<( test_case + 1 )<<":"<<std::endl;
    
    scanf("%i %i", &data[test_case][0], &data[test_case][1]);
    //std::cout<<data[test_case][0]<<" "<<data[test_case][1]<<std::endl;
    
    //std::cout<<std::endl;
  }
  
  // output
  
  //std::cout<<"Output: "<<std::endl<<std::endl;
  
  for ( int test_case = 0; test_case < n_test_cases; test_case++ )
  {
    int count = 0;
    
    std::cout<<"Case #"<<( test_case + 1 )<<": ";
    
    
    for ( int low = data[test_case][0]; low <= data[test_case][1]; low++ )
    {
      if ( isFairAndSquare( low ) )
      {
        count++;
      }
    }
    
    std::cout<<count<<std::endl;
  }
  return 0;
}

bool isPalindrome( int number )
{
  std::string numberString, rNumberString;
  std::ostringstream convert;
  
  // convert number to string
  convert << number;
  numberString = convert.str();
  rNumberString = numberString;
  
  std::reverse( rNumberString.begin(), rNumberString.end() );
  
  if ( numberString.compare(rNumberString) == 0 )
  {
    return true;
  }
  
  return false;
}

bool isFairAndSquare( int number )
{
  double d_sqrt;
  int i_sqrt;
  
  // check if number is a palindrome
    if ( isPalindrome( number ) )
    {
      
      // check if number is a square
      d_sqrt = sqrt( number );
      i_sqrt = d_sqrt;
      
      if ( d_sqrt == i_sqrt )
      {
      
        // check if the square root is a palindrome
        if ( isPalindrome( sqrt( number ) ) )
        {
          return true;
        }
        
      }
      
    }
  
  return false;
}
