#include <iostream>   
#include <fstream>    
#include <stdlib.h>   // atoi
#include <string>     
using namespace std;  
#include <list>
#include <sstream>;

bool emptySquareFound;
bool tomekFound;
char winner;
bool gameWon;

void checkString(string);
 
int main()
{
  ifstream in ("A-small-attempt0.in");         
  ofstream out("output.out");         
  if (!in.is_open() || in.eof() )             
  {
    cerr << "ERROR: invalid input file" << endl;
    return (-1);
  }
  if(!out.is_open())                            
  {
    cerr << "ERROR: couldn't create ouput file" << endl;
    return (-1);
  }
 
  //list<string> string_list;
  int numCases;                       
  
  string rowA;
  string rowB;
  string rowC;
  string rowD;
  string emptyLine;

  string columnA;
  string columnB;
  string columnC;
  string columnD;

  string diagonalA;
  string diagonalB;

  std::string line;
                        
  getline( in, line, '\n' );           
  numCases = atoi( line.c_str() );      
 
  for (int c=1; c<=numCases; c++)               
  {
	rowA = "";
	rowB = "";
	rowC = "";
	rowD = "";

	columnA = "";
	columnB = "";
	columnC = "";
	columnD = "";

	diagonalA = "";
	diagonalB = "";


	emptySquareFound = true;
    tomekFound = false;
	gameWon = false;

	std::getline(in, rowA);  
	std::getline(in, rowB);
	std::getline(in, rowC);
	std::getline(in, rowD);
	std::getline(in, emptyLine);
	
	// check for an empty square
	if ( (rowA.find('.') == -1) && (rowB.find('.') == -1) && (rowC.find('.') == -1) && (rowD.find('.') == -1) ) 
	{ 
		emptySquareFound = false;
	}

	// check rows for a winner
	checkString(rowA);
	if (gameWon == false)
		checkString(rowB);
	if (gameWon == false)
		checkString(rowC);
	if (gameWon == false)
		checkString(rowD);

	// check columns
	if (gameWon == false)
	{
		columnA.append(1, rowA[0]);
		columnA.append(1, rowB[0]);
		columnA.append(1, rowC[0]);
		columnA.append(1, rowD[0]);

		checkString(columnA);	
	}

	if (gameWon == false)
	{
		columnB.append(1, rowA[1]);
		columnB.append(1, rowB[1]);
		columnB.append(1, rowC[1]);
		columnB.append(1, rowD[1]);

		checkString(columnB);	
	}

	if (gameWon == false)
	{
		columnC.append(1, rowA[2]);
		columnC.append(1, rowB[2]);
		columnC.append(1, rowC[2]);
		columnC.append(1, rowD[2]);

		checkString(columnC);	
	}

	if (gameWon == false)
	{
		columnD.append(1, rowA[3]);
		columnD.append(1, rowB[3]);
		columnD.append(1, rowC[3]);
		columnD.append(1, rowD[3]);

		checkString(columnB);	
	}

	// check diagonals
	if (gameWon == false)
	{
		diagonalA.append(1, rowA[0]);
		diagonalA.append(1, rowB[1]);
		diagonalA.append(1, rowC[2]);
		diagonalA.append(1, rowD[3]);

		checkString(diagonalA);
	}

	if (gameWon == false)
	{
		diagonalB.append(1, rowA[3]);
		diagonalB.append(1, rowB[2]);
		diagonalB.append(1, rowC[1]);
		diagonalB.append(1, rowD[0]);

		checkString(diagonalB);
	}

	//gameCompleted = true;

	out << "Case #" << c << ": ";
	if ( gameWon == true)
		out << winner << " won";
	else if ( (gameWon == false) && (emptySquareFound == true) )
		out << "Game has not completed";
	else if ( (gameWon == false) && (emptySquareFound == false) )
		out << "Draw";
	
	out << endl;

  }
  in.close();       
  out.close();    
 
  return 0;
}

void checkString(string a)
{
	char temp = a[0];
	if (temp == 'T')
		temp = a[1];
	if (temp != '.')
	{
		int count = 1;
		for (int i = 1; i < 4; i++)
		{
			if (a[i] == 'T')
			{
				tomekFound = true;
				continue;
			}

			if (a[i] == temp)
			{
				count++;
			}
		}

		if (tomekFound == true)
		{
			if (count == 3)
			{
				winner = temp;
				gameWon = true;
			}
		}
		else
		{
			if (count == 4)
			{
				winner = temp;
				gameWon = true;
			}
		}
	
		if (gameWon == false)
		{ // reset tomek
			tomekFound = false;
		}
	}
}

