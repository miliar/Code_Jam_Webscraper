/** 
 * Kirsten Erich (kirstee)
 *
 * Google Code Jam
 *
 * Fair.cpp
 * 
 * Program to test if given number is a "fair square" - meaning it has
 *  a whole number square root AND the value and the value's square root are
 *  number palindromes 
 * 
 * April 5, 2012
 * 1:38 PM
 * 
**/

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <time.h>
#include <string.h>
#include <stdio.h>
#include <iosfwd>
#include <math.h>

using namespace std;

/* testPalindrome - uses division and mod division to test if the square is a palindrome */
bool testPalindrome (int a, ofstream & outfile){

   int remain = 0;

   if (a > 99){

      remain = a%10;
      a = a/10;

      if (a/10 == remain){

         return true;

      }
      else {
         return false;
      }

   } // if three digits

   else if (a > 9){

      remain = a%10;

      if (a/10 == remain){

         return true;

      }
      else {
         return false;
      }
      

   } // if two digits

   else {

      return true;

   } // if one digit

} // testPalindrome


/* ------------------------------------------------ */

int main (int argc, char *argv[]) {

   // initialize variables
   int size = 0, ct = 0, value = 0, temp = 0, result = 0;
   int lowerLimit = 0, upperLimit = 0;

   double square = 0;

   // declare and initialize infile and outfile
   ifstream infile (argv[1]);
   ofstream outfile (argv[2]);

   // store first int (from infile) into size
   infile >> size;

   while (ct < size){

      infile >> lowerLimit;
      infile >> upperLimit;
      value = lowerLimit;

      /* generate output for each case */
      outfile << "Case #" << ct+1 << ": ";

      while (value < upperLimit + 1){

         square = sqrt(value);

         if ( square - (int)square == 0 ){

            temp = (int) square; // store the square in an int

            if ( testPalindrome (temp, outfile) ){

               if ( testPalindrome (temp*temp, outfile) ){

                  result++;

               } // test palindrome of value

            } // test palindrome of sqrt (value)

         } // if the value is a square

         value ++;

      } // while - test all the values within the limits

      outfile << result << endl;

      result = 0;

      ct++;

   } // while

   return 0;

} // main
