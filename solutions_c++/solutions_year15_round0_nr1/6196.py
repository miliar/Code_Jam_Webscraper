//Written by Jorge Beltran
//takes an input file named Audience.in
//Outputs to InviteFriends.txt
//Input needs to be in the same folder as program.

#include <fstream>
using namespace std;

int main()
{
  //define variables
  ifstream fin;
  ofstream fout;
  int NCases;  
  int SMax;
  int* Cases;


  //open Audience text file.
  fin.open("Audience.in");
  if(!fin.good()) throw "I/O error";

  //Get the first line, which is the number of cases.
  fin >> NCases;
  fin.ignore(1000, 10);


  //Create an int array with size n for the number of cases. This will store the answers.
  Cases = new int[NCases];

  for(int i = 0; i < NCases; i++)
  {
    //Case logic
    //Stores the number of people applausing before the last.
	int Friends = 0;
	int Extras = 0;

    //temp variables.
    int temp = 0;

    //read the first number. This is Smax.
    fin >> SMax;
    fin.ignore(1000, ' ');



    //Add all the numbers together excluding the Smax level.
    for(int z = 0; z < SMax; z++)
    {
	  temp = int(fin.get()) - 48;  // convert char to int
	  if (0 == temp)
	  {
		  if (Extras > 0)
		  {
			  Extras--;
		  }
		  else
		  {
			  Friends++;
		  }
	  }
	  else if (temp > 1)
	  {
		  Extras += (temp - 1);
	  }


    }

    //save the number of friends
	Cases[i] = Friends;

    //burn the last char.
    fin.get();
  }

  //close the file.
  fin.close();

//output

  //open a file
  fout.open("InviteFriends.txt");

  //for each line, write "Case#" N ":" int people to invite.
  for(int i = 0; i < NCases; i++)
  {
    fout << "Case #" << i + 1 << ": " << Cases[i] << endl;
  }

  //close the file.
  fout.close();  

  //delete new stuff.
  delete [] Cases;


  return 0;

}