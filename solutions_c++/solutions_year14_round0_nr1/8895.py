//by Lilli Christoph
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
// #include <algorithm>
// #include <map>
// #include <cstdlib>
// #include <cmath>

using namespace std;

int main(void)
{
  int numCases, gameSize=4;
  vector <int> initialRow, finalRow;
  vector <int> myCard;
  int r1, r2, cardValue;

  string inputfile = "A-small-attempt0.in";
  string cheater="Volunteer cheated!", badMagic="Bad magician!";
 
  //Load input from file
  ifstream inputFile(inputfile.c_str());
  inputFile >> numCases;
 
  //Get case data
  for(int c=0; c<numCases; c++)
    {
      inputFile >> r1;
      for(int i=0; i<gameSize; i++)
	  for(int j=0; j<gameSize; j++)
	    {
	     inputFile >> cardValue;
	     if(i== r1-1)
	       initialRow.push_back(cardValue);
	    }

      inputFile >> r2;
      for(int i=0; i<gameSize; i++)
	for(int j=0; j<gameSize; j++)
	  {
	    inputFile >> cardValue;
	    if(i== r2-1)
	      finalRow.push_back(cardValue);
	  }
      for(int i=0; i<gameSize; i++)
	for(int j=0; j<gameSize; j++)
	  if(initialRow[i]==finalRow[j])
	    myCard.push_back(initialRow[i]);

      //OutputResults
	cout << "Case #" << c+1 << ": ";
	if(myCard.size()==1)
	  cout << myCard[0] << endl;
	if(myCard.size()>1)
	  cout << badMagic << endl;
	if(myCard.size()==0)
	  cout << cheater << endl;

	myCard.clear();
	initialRow.clear();
	finalRow.clear();
    }

  return 0;
}
