/*Small input
9 points	
You may try multiple times, with penalties for wrong submissions.
Large input
12 points	
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

At the Infinite House of Pancakes, there are only finitely many pancakes, but there are infinitely many diners who would be willing to eat them! When the restaurant opens for breakfast, among the infinitely many diners, exactly D have non-empty plates; the ith of these has Pi pancakes on his or her plate. Everyone else has an empty plate.

Normally, every minute, every diner with a non-empty plate will eat one pancake from his or her plate. However, some minutes may be special. In a special minute, the head server asks for the diners' attention, chooses a diner with a non-empty plate, and carefully lifts some number of pancakes off of that diner's plate and moves those pancakes onto one other diner's (empty or non-empty) plate. No diners eat during a special minute, because it would be rude.

You are the head server on duty this morning, and it is your job to decide which minutes, if any, will be special, and which pancakes will move where. That is, every minute, you can decide to either do nothing and let the diners eat, or declare a special minute and interrupt the diners to make a single movement of one or more pancakes, as described above.

Breakfast ends when there are no more pancakes left to eat. How quickly can you make that happen?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with D, the number of diners with non-empty plates, followed by another line with D space-separated integers representing the numbers of pancakes on those diners' plates.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the smallest number of minutes needed to finish the breakfast.
Limits

1 ? T ? 100.
Small dataset

1 ? D ? 6.
1 ? Pi ? 9.
Large dataset

1 ? D ? 1000.
1 ? Pi ? 1000.
Sample

Input
  	
Output
 

3
1
3
4
1 2 1 2
1
4

	

Case #1: 3
Case #2: 2
Case #3: 3

In Case #1, one diner starts with 3 pancakes and everyone else's plate is empty. One optimal strategy is:

Minute 1: Do nothing. The diner will eat one pancake.

Minute 2 (special): Interrupt and move one pancake from that diner's stack onto another diner's empty plate. (Remember that there are always infinitely many diners with empty plates available, no matter how many diners start off with pancakes.) No pancakes are eaten during an interruption.

Minute 3: Do nothing. Each of those two diners will eat one of the last two remaining pancakes.

In Case #2, it is optimal to let the diners eat for 2 minutes, with no interruptions, during which time they will finish all the pancakes.

In Case #3, one diner starts with 4 pancakes and everyone else's plate is empty. It is optimal to use the first minute as a special minute to move two pancakes from the diner's plate to another diner's empty plate, and then do nothing and let the diners eat for the second and third minutes. 
*/
// 0.0 open in and out files.
// 1.0 read number of test cases and print result.
// 2.0 Loop over each case:   
   // 2.1 read # of diners with packcakes
      

   // 2.2 loop over to read panckes counts
      
      // 2.2.1 fill array.

      // 2.2.2 update max_pancake count.

  //  2.3 loop over solution setup.
      
      // 2.3.1 loop setup set define moves count to 0.

      // 2.3.2 define min_time to be max_pancake count. 



  //  2.4 Loop over pancake_target from 1 to max_pancake count.
     // 2.4.1 setup for loop over plates that have pancakes.

     // 2.4.2 Loop over all plates that have pancakes 

        // 2.4.2.1 while a plate has more pancake_target do moves.

    // 2.4.3 add moves and pancake_target in total_time

    // 2.4.4 If min_time is less then set to new min_time. 

   
   // 2.5 Print solution.

// 10.0 Close output file and end program



#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;
int verbose = 0;

void end_program (int exit_code)
{
		cout << "\n Press Return two times to exit the program \n";
		cin.clear();
		cin.ignore(255, '\n');
		cin.get();
        exit(exit_code);
}

int _tmain(int argc, _TCHAR* argv[])
{
  // 0.0 open in and out files.
    if (verbose) { cout << "start of run code \n"; }
	
    if (verbose) { cout << "0.0 Read in.dat file\n"; };
    //ifstream inf("in.dat");
    //ifstream inf("B-small-attempt0(1).in");
    ifstream inf("B-large.in");

    // If we couldn't open the output file stream for reading
      if (!inf)
        {
          // Print an error and exit
          cerr << "Uh oh, in.dat could not be opened for reading!" << endl;
          end_program(1);
        }
  // 1.0 read number of test cases and print result.
	 int test_number; // number of test cases.int T
	 inf >> test_number;
    
	 if (verbose) { cout << "number of test cases N: " << test_number << endl; };
	
   	 // 1.1 open output file:
       ofstream outf("out.txt");
      // If we couldn't open the output file stream for reading exit
        if (!outf)
        {
          // Print an error and exit
          cerr << "Uh oh, out.txt could not be opened for writing!\n" << endl;
          end_program(1);
	    }	
  // 2.0 Loop over each case:   
	if (verbose) { cout << "2.0 Start of main loop\n"; }
	for (int test_num = 1; test_num <= test_number  ; test_num++ ) 
	{
      // 2.1 read # of diners with packcakes
      int diners_count = 0;
	  inf >> diners_count ;

      // 2.2 loop over to read panckes counts
	   int plate[1010] ; // allow to be 1010 plates.
	   int max_pancakes = 1; // there at least 1 pancake.
       for (int iii = 1 ; iii <= diners_count ; iii++ )
        {
         // 2.2.1 fill array.
	       inf >> plate[iii];
		 
         // 2.2.2 update max_pancake count.
		   if (plate[iii] > max_pancakes ) 
		   { 
			  max_pancakes = plate[iii]; 
		      if (verbose >= 3) { cout << "new_max_pancakes: " << max_pancakes << endl; };
		   }
		   if (verbose >= 4) { cout << "plate[" << iii << "]=" << plate[iii] << endl; };
		}   
        
      //  2.3 loop over solution setup.
      
        

        // 2.3.2 define min_time to be max_pancake count. 
          int min_time = max_pancakes ;

     //  2.4 Loop over pancake_target from 1 to max_pancake count.
         for ( int pancake_target = 1; pancake_target <= max_pancakes; pancake_target++)
		 { 
		   // 2.4.1 setup for loop over plates that have pancakes.
             // 2.4.1.. loop setup set define moves count to 0.
		       int moves = 0;

             // 2.4.2 Loop over all plates that have pancakes 
               for ( int current_plate = 1 ; current_plate <= diners_count ; current_plate++)
			   {
			     // 2.4.2.1 while a plate has more pancake_target do moves.
                  int pancake_count = plate[current_plate];
			      while ( pancake_count > pancake_target )
				  {
                     moves++;
				     pancake_count = pancake_count - pancake_target; 
					 if (verbose > 2) { cout << "#" << test_num << " moveing: " << pancake_target << " from plate: " << current_plate << endl; };
				  };
			   };
             // 2.4.3 add moves and pancake_target in total_time
             int total_time = moves + pancake_target;

             // 2.4.4 If min_time is less then set to new min_time. 
			 if ( total_time < min_time )
			 {
               min_time = total_time;
				   if (verbose) { cout << "#" << test_num << " new min_time: " << min_time << " moves: " << moves << " target: " << pancake_target << endl; };

			 };		  

		 } 
     // 2.5 Print solution.
         outf << "Case #" << test_num << ": " << min_time << endl;
         cout << "Case #" << test_num << ": " << min_time << endl;
	}


  // 10.0 Close output file and end program
    outf.close(); 
    end_program(0);

	return 0;
}

