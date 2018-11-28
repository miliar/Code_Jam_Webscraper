/*
 * Problem-C-Fair-and-Square.cpp
 *
 *  Created on: 14.04.2013
 *      Author: XStalkerX
 */

#include <fstream>
#include <iostream>

#include <vector>
#include <string>
#include <sstream>

bool isFair (unsigned long long number)
{
  std::stringstream n;
  n << number;
  std::string numstr = n.str();
  for (int i = 0; i <= numstr.size()/2; ++i )
  {
    if (numstr[i] != numstr[numstr.size() - i - 1])
      return false;
  }

  return true;
}

int main (int argc, char* argv[])
{
  if (argc != 2)
  {
    std::cout << "No file" << std::endl;
    return 0;
  }

  std::ifstream input (argv[1], std::fstream::in);
  if (!input.is_open())
  {
    std::cout << "Can't read" << std::endl;
    return -1;
  }

  std::ofstream output ("FairAndSquare.out", std::fstream::out);
  if (!output.is_open())
  {
    std::cout << "Can't write" << std::endl;
    return -1;
  }


  int cases_number = 0;
  input >> cases_number;

  std::vector <unsigned long long> fairsquares;

//      This code was used to precalculate Fair and Square
//          values from 1 to 10^15.
//
//
//  for (unsigned long long possible = 1; ; ++possible)
//  {
//
//    if (!isFair(possible))
//      continue;
//
//    unsigned long long square = possible * possible;
//
//    if (square > 1000000000000000)
//      break;
//
//    if (isFair(square))
//      fairsquares.push_back(square);
//  }
  fairsquares.push_back(1);
  fairsquares.push_back(4);
  fairsquares.push_back(9);
  fairsquares.push_back(121);
  fairsquares.push_back(484);
  fairsquares.push_back(10201);
  fairsquares.push_back(12321);
  fairsquares.push_back(14641);
  fairsquares.push_back(40804);
  fairsquares.push_back(44944);
  fairsquares.push_back(1002001);
  fairsquares.push_back(1234321);
  fairsquares.push_back(4008004);
  fairsquares.push_back(100020001);
  fairsquares.push_back(102030201);
  fairsquares.push_back(104060401);
  fairsquares.push_back(121242121);
  fairsquares.push_back(123454321);
  fairsquares.push_back(125686521);
  fairsquares.push_back(400080004);
  fairsquares.push_back(404090404);
  fairsquares.push_back(10000200001);
  fairsquares.push_back(10221412201);
  fairsquares.push_back(12102420121);
  fairsquares.push_back(12345654321);
  fairsquares.push_back(40000800004);
  fairsquares.push_back(1000002000001);
  fairsquares.push_back(1002003002001);
  fairsquares.push_back(1004006004001);
  fairsquares.push_back(1020304030201);
  fairsquares.push_back(1022325232201);
  fairsquares.push_back(1024348434201);
  fairsquares.push_back(1210024200121);
  fairsquares.push_back(1212225222121);
  fairsquares.push_back(1214428244121);
  fairsquares.push_back(1232346432321);
  fairsquares.push_back(1234567654321);
  fairsquares.push_back(4000008000004);
  fairsquares.push_back(4004009004004);
  fairsquares.push_back(100000020000001);
  fairsquares.push_back(100220141022001);
  fairsquares.push_back(102012040210201);
  fairsquares.push_back(102234363432201);
  fairsquares.push_back(121000242000121);
  fairsquares.push_back(121242363242121);
  fairsquares.push_back(123212464212321);
  fairsquares.push_back(123456787654321);
  fairsquares.push_back(400000080000004);

//  for (int i = 0; i < fairsquares.size(); ++i)
//    std::cout << fairsquares[i] << std::endl;

  for (int case_n = 1; case_n <= cases_number; case_n++)
  {
    unsigned long long a;
    unsigned long long b;
    input >> a;
    input >> b;
    int total = 0;

    for (int i = 0; i < fairsquares.size(); ++i)
    {
      if (a <= fairsquares[i] and
          b >= fairsquares[i])
        total++;
    }

    if (case_n != 1)
      output << std::endl;
    output << "Case #" << case_n << ": " << total;
  }

  input.close();
  output.close();
}



