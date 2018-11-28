#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>

/*
Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ C ≤ 500.
1 ≤ F ≤ 4.
1 ≤ X ≤ 2000.
Large dataset

1 ≤ C ≤ 10000.
1 ≤ F ≤ 100.
1 ≤ X ≤ 100000.

decimal precision = 7
total precison = 6+7 =13
*/

#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

#define PRECISION 7

using namespace std;

fstream fin, fout;
int testcases, t;
// C: cost of farm
// X: cookies to win
// F: extra cookies with new farm
double CostOf_Farm, F, X;

// cps : cookies per second, cookiesToWin = cookies to win
// return time taken
double play(double cookiesToWin, double cps);

int main()
{
   fin.open(INPUT_FILE, ios::in);
   fout.open(OUTPUT_FILE, ios::out);

   fout << fixed << setprecision(PRECISION);   
   cout << fixed << setprecision(PRECISION);   

   fin >> testcases;
   
   for(t=1; t<=testcases; t++)
   {
      fin >> CostOf_Farm >> F >> X ;
      // cout << CostOf_Farm << " " << F << " " << X << endl;
      double time=0;
      time = play(X, 2);   // x= total cookies to win; initial cps = 2
  
      // cout << time << endl; 
      fout << "Case #" << t << ": " << time << endl;
   } 
   
   fout.close();
   fin.close();   
   return 0;
}

double play(double cookiesToWin, double cps)
{
   double pt=0;
   double local_time=0, score=0, sec=0, t;
   
   while(1)
   {
      sec=sec+1;
      score = (cps)*sec;

      if(score >= CostOf_Farm)
         break;
   }
   
   if(score >= CostOf_Farm)
   {

      if((cookiesToWin/cps) > ( CostOf_Farm/cps + cookiesToWin/(cps+F)) ) 
      {
         local_time = CostOf_Farm/cps;
         // with purchasing new farm
//         cout << local_time << endl;
         pt = play(cookiesToWin, cps+F);
      }
      else
      {
         local_time = cookiesToWin/cps;
//         cout << "End: " << local_time << endl;
      }
   
   }

   local_time = local_time + pt;

   return local_time;
}

