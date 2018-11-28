/*
Small input
7 points	
You may try multiple times, with penalties for wrong submissions.
Large input
10 points	
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

It's opening night at the opera, and your friend is the prima donna (the lead female singer). You will not be in the audience, but you want to make sure she receives a standing ovation -- with every audience member standing up and clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a shyness level. An audience member with shyness level Si will wait until at least Si other audience members have already stood up to clap, and if so, she will immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately, regardless of what anyone else does. For example, an audience member with Si = 2 will be seated at the beginning, but will stand up to clap later after she sees at least two other people standing and clapping.

You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the prima donna to be in the audience to ensure that everyone in the crowd stands up and claps in the end. Each of these friends may have any shyness value that you wish, not necessarily the same. What is the minimum number of friends that you need to invite to guarantee a standing ovation?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience, followed by a string of Smax + 1 single digits. The kth digit of this string (counting starting from 0) represents how many people in the audience have shyness level k. For example, the string "409" would mean that there were four audience members with Si = 0 and nine audience members with Si = 2 (and none with Si = 1 or any other value). Note that there will initially always be between 0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of friends you must invite.
Limits

1 ? T ? 100.
Small dataset

0 ? Smax ? 6.
Large dataset

0 ? Smax ? 1000.
Sample

Input
  	
Output
 

4
4 11111
1 09
5 110011
0 1

	

Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0

In Case #1, the audience will eventually produce a standing ovation on its own, without you needing to add anyone -- first the audience member with Si = 0 will stand up, then the audience member with Si = 1 will stand up, etc.

In Case #2, a friend with Si = 0 must be invited, but that is enough to get the entire audience to stand up.

In Case #3, one optimal solution is to add two audience members with Si = 2.

In Case #4, there is only one audience member and he will stand up immediately. No friends need to be invited.
*/


// code plan:
// 0.0 start of loop reading each test case.
// 1.0 read number of test cases and print result.
// 2.0 Loop over each case:  

// 2.1 read shy_max from input

// 2.2 loop to read people shy levels

// 10.0 Close output file and end program



#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int verbose = 1;
// define max size of array of shy people.
#define MAX_SIZE = 1010;


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
  // 0.0 loop reading each test case.
    if (verbose) { cout << "start of run code \n"; };
	
    if (verbose) { cout << "Read in.dat file\n"; };
    //ifstream inf("in.dat");
    //ifstream inf("A-small.in");
    ifstream inf("A-large-attempt.in");

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
  
      // 2.1 read shy_max from input
       int shy_max;
       inf >> shy_max;
	   if (verbose >= 2) { cout << "shy_max: " << shy_max << endl; };
	  // 2.2 loop to read people shy levels
        char one_char ;
        // read space before shy numbers.
          one_char = inf.get(); 
        // intiger to keep # of people in ad
		int shy_array[ 1010 ];
        for (int iii = 0; iii <= shy_max  ; iii++ )
        {
         // Get one character out of io steam
	       one_char = inf.get();
		 // convert one_char to intiger by subtracting the asic code of 0 from one_char
		   shy_array[iii] = one_char - '0';
		   if (verbose >= 3) { cout << "one_char: " << one_char << endl; };
		   if (verbose >= 3) { cout << "shy_array[" << iii << "]: " << shy_array[iii] << endl; };
		}   
	   // 2.3.0 loop over shy level array to find stick points. and add people
         
		// 2.3.1 Loop veriable setup
           int friend_count = 0;
           int people_standing = 0;      
		   // 2.3.2 Start loop over # of people stand up.
            for (int shy_level = 0; shy_level <= shy_max  ; shy_level++ )
			{
              // 2.3.2.1 check to see people will stand up.
                if (shy_level <= people_standing) 
				{
                  // Add shy_level people to people standing
					people_standing += shy_array[shy_level];
				}
				else
				{	
				  // 2.3.2.1.1 If we are stuck add friends to get unstuck
                    friend_count++ ;  // add a friend.
					people_standing++ ; // Because shy level is increased by 1 in each loop we only need one more person to make standing_people = shy_level
                    people_standing += shy_array[shy_level] ; // With added friend now shy people stand. 
				};
				if (verbose >= 2) { cout << "shy: " << shy_level << " p_st: " << people_standing << " F#: " << friend_count << endl; };    
			}
        // 2.4 Print result
         outf << "Case #" << test_num << ": " << friend_count << endl; 
         cout << "Case #" << test_num << ": " << friend_count << endl;
	}


// 10.0 Close output file and end program
    outf.close(); 
    end_program(0);

	return 0;
}

