//Written by Jorge Beltran
//Takes Omino.in as input
//Outputs GameWinners.txt
//Assumes that Richard will make holes with N greater than 6.

#include <fstream>
using namespace std;

int main()
{
  //declare variables.  
  ifstream fin;
  int NCases;  
  bool* Cases;

  //read input file.
  fin.open("Omino.in");
  if(!fin.good()) throw "I/O error";  

  //get the number of cases.
  fin >> NCases;
  fin.ignore(1000, 10);

  //Create a bool array.
  Cases = new bool[NCases];
 
  for(int i = 0; i < NCases; i++)
  {
    //variables
    int NBlocks;
    int Rows;
    int Columns;
    bool GabrielWins = true;

    fin >> NBlocks;
    fin >> Rows;
    fin >> Columns;



  //if >= 7, the chosen piece can have a hole, which will make it a loss.
  if(NBlocks >= 7 )
  {
    GabrielWins = false;
  }
  //check if it will never fill all the spots
  else if((Rows * Columns) % NBlocks)
  {
    GabrielWins = false;
  }
  else
  {
    //try to make a piece not fit.
    int length = NBlocks;
    int width = 1;  
    for(;width <= length; length--, width++)
    {
      if((length > Rows || width > Columns ) && (length > Columns || width > Rows))
      {
        GabrielWins = false;
        break;
      }
    }

    //test these cases that the loop misses.
    //case #1, 4-omino. Grid 4n x 2.
    if(NBlocks == 4 && (Rows == 2 || Columns == 2))
      GabrielWins = false;
    //case #2, 5-omino. Grid 5n x 3.
    if(NBlocks == 5 && (Rows == 3 || Columns == 3))
      GabrielWins = false;
    //Case #3, 6-omino. Grid 6n x 3.
    if(NBlocks == 6 && (Rows == 3 || Columns == 3))
      GabrielWins = false;
  }
    
    Cases[i] = GabrielWins;

  }

  //close file.
  fin.close();
  

  //output
  //Open new file
  ofstream fout;
  fout.open("GameWinners.txt");

  //output loop
  for(int i = 0; i < NCases; i++)
  {
    fout << "Case #" << i+1 << ": ";
    if(Cases[i])
      fout << "GABRIEL";
    else
      fout << "RICHARD";
    fout << endl;
  }

  //delete new stuff
  delete [] Cases;


  return 0;
}