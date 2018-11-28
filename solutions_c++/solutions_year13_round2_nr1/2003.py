//by Lilli Christoph
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
// #include <map>
// #include <cstdlib>
 #include <cmath>

using namespace std;

int main(void)
{
  int numCases, numMotes, numMoves=0, maxMoves, deltaM;
  vector <int> motes;
  int myMote;

  string inputfile = "A-large.in";
 
  //Load input from file
  ifstream inputFile(inputfile.c_str());
  inputFile >> numCases;
  //cout << "numcases is " << numCases << endl;
  //Get case data
  for(int c=1; c<numCases+1; c++)
    {
      inputFile >> myMote;
      inputFile >> numMotes;
      maxMoves = numMotes;
      //cout << "myMote is size " << myMote << " and there are " << numMotes << " motes around" << endl;
      for(int i=0; i<numMotes; i++)
	motes.push_back(0);
      for(int i=0; i<numMotes; i++)
	inputFile >> motes[i];
      sort(motes.begin(), motes.end());

       // for(int i=0; i<numMotes; i++)
       // 	 cout << motes[i] << " ";
       // cout << endl;

       for(int i=0; i<numMotes; i++)
	 {
	   if(myMote > motes[i])
	     {
	       myMote = myMote + motes[i];
	       continue;
	     }
	   //couldn't absorb, now do stuff
	   // mote is too small to absorb anything
	   if(myMote <= 1)
	     {
	     numMoves = numMoves + numMotes-i;
	     break;
	     }

	   deltaM = motes[i] - myMote;
	   if(deltaM >= (pow(2, numMotes-i)*(myMote-1) + 1))
	     {
	       numMoves = numMoves + numMotes-i;
	       break;
	     }

	   maxMoves = min(maxMoves, numMoves+numMotes-i);
	   //add motes to beef up
	   while(myMote <= motes[i])
	     {
	       numMoves++;
	       myMote = 2*myMote - 1;
	     }
	   myMote = myMote + motes[i];
	 
	   if(numMoves >= maxMoves)
	     {
	       numMoves = maxMoves;
	       break;
	     }
	 }
      //OutputResults

      cout << "Case #" << c << ": " << numMoves << endl;
 
      motes.clear();
      numMoves = 0;

    }
  return 0;
}
