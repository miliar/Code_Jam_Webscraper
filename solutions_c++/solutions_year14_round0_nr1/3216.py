#include <iostream>
#include <fstream>
#include <cstring>

/*
    Limits

    1 ≤ T ≤ 100.
    1 ≤ both answers ≤ 4.
    Each number from 1 to 16 will appear exactly once in each arrangement. 
*/

//#define INPUT_FILE "input.txt"
#define INPUT_FILE "A-small-attempt0.in"
#define OUTPUT_FILE "output.txt"
#define SIZE 4

using namespace std;



fstream fin, fout;
int testcases, t;
int arrange1[SIZE][SIZE];
int arrange2[SIZE][SIZE];
int selection1=-1, selection2=-1;
int row, col;


int main()
{
   fin.open(INPUT_FILE, ios::in);
   fout.open(OUTPUT_FILE, ios::out);
   
   fin >> testcases;
   
   for(t=1; t<=testcases; t++)
   {
      fin >> selection1;
      
      // get first arrangement
      for(row=0; row<SIZE; row++)
      {
         for(col=0; col<SIZE; col++)
         {
            fin >> arrange1[row][col];
         }
      }

      fin >> selection2;

      // get second arrangement
      for(row=0; row<SIZE; row++)
      {
         for(col=0; col<SIZE; col++)
         {
            fin >> arrange2[row][col];
         }
      }

      //check if two selected row are having only one match, or No mach, or multiple matches;      

      int match = 0;
      int found = -1;
      for(int i=0; i<SIZE; i++)
      {
         for(int j=0; j<SIZE; j++)
         {
            if(arrange1[selection1 - 1][i] == arrange2[selection2 - 1 ][j])
            {
               match++;
               found = arrange1[selection1 - 1][i];
            }
         }
      }

      if(match == 1)
      {
         cout << "Case #" << t << ": " << found << endl;
      }
      else if(match > 1)
      {
         cout << "Case #" << t << ": " << "Bad magician!" << endl;
      }
      else if(match == 0)
      {
         cout << "Case #" << t << ": " << "Volunteer cheated!" << endl;
      }
      else
      {
         cout << "Something went wrong. Check you code !!!" << endl;
      }

   } 
   
   fout.close();
   fin.close();   
   return 0;
}

