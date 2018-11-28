#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

/*
  Limits

  1 ≤ T ≤ 50.
  All the masses given to Ken and Naomi are distinct, and between 0.0 and 1.0 exclusive.
  Small dataset

  1 ≤ N ≤ 10.
  Large dataset

  1 ≤ N ≤ 1000.
*/

#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

using namespace std;


int testcases, t;
fstream fin, fout;

int b, numBlocks=0;
float f;

int main()
{
   
   fin.open(INPUT_FILE, ios::in);
   fout.open(OUTPUT_FILE, ios::out);

   fin >> testcases;

   for(t=1; t<=testcases; t++)
   {
      fin >> numBlocks;
      vector<float> us_naomi; //unsorted
      vector<float> us_ken;   //unsorted
      
      vector<float>::iterator iter;

      //Get Naomis block
      for(b=0; b<numBlocks; b++)
      {
         fin >> f;
         us_naomi.push_back(f);
      }
      
      //Get Kens block
      for(b=0; b<numBlocks; b++)
      {
         fin >> f;
         us_ken.push_back(f);
      }

      vector<float> naomi(us_naomi);
      vector<float> ken(us_ken);

      sort(naomi.begin(), naomi.end());
      sort(ken.begin(), ken.end());

#if 0
      cout << "Naomi:  ";
      for(iter=naomi.begin(); iter!=naomi.end(); iter++)
      {
         cout << *iter << "  ";
      }
      cout << endl;

      cout << "Ken:    ";
      for(iter=ken.begin(); iter!=ken.end(); iter++)
      {
         cout << *iter << "  ";
      }
      cout << endl;
#endif

      int kenWin=0, naomiWin=0;
      int i, j;
      for(j=0, i=0; (i<numBlocks && j<numBlocks); )
      {
//         cout << ken[j] << " " << naomi[i] << endl;
         if(ken[j] > naomi[i])
         {
            i++;
            j++;
            kenWin++;
         }
         else
         {
            j++;
         }
      }
      naomiWin = numBlocks - kenWin;

//      cout << naomiWin << endl;
   
      int kenDeceitWin=0, naomiDeceitWin=0;
      for(j=0, i=0; (i<numBlocks && j<numBlocks); )
      {
//         cout << ken[j] << " " << naomi[i] << endl;
         if(naomi[i] > ken[j])
         {
            i++;
            j++;
            naomiDeceitWin++;
         }
         else
         {
            i++;
         }
      }

//      cout << naomiDeceitWin << endl;
   
      fout << "Case #" << t << ": " << naomiDeceitWin << " " << naomiWin << endl;

   }
   fout.close();
   fin.close();
   return 0;
}
