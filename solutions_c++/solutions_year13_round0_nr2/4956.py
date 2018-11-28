//by Lilli Christoph
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main(void)
{
  vector < vector <int> > lawn;
  vector <int> yardSize(2,0);
  vector <vector <int> > lawnCols;
  int maxRowHeight, maxColHeight;
  int numCases=0, status=0;
  string inputfile = "B-large.in";
  string output1="Case #", outputPass=": YES", outputFail=": NO";
  ifstream inputFile(inputfile.c_str());
  inputFile >> numCases; 
  //Get case data
  for(int c=1; c<numCases+1; c++)
    {
      for(int dim=0; dim<2; dim++)
	inputFile >> yardSize[dim];

      for(int N=0; N<yardSize[0]; N++)
	{
	  lawn.push_back(vector <int> (yardSize[1], 0));
	  for(int M=0; M<yardSize[1]; M++)
	    inputFile >> lawn[N][M];
	}
      //this feels a little dirty
      for(int M=0; M<yardSize[1]; M++)
	{
	  lawnCols.push_back(vector <int> (yardSize[0], 0));
	  for(int N=0; N<yardSize[0]; N++)
	    lawnCols[M][N] = lawn[N][M];
	}

      //Have all data set up.
      //Now analyze LAWN!
      for(int i=0; i<yardSize[0]; i++)
	{
	  maxRowHeight = *max_element(lawn[i].begin(), lawn[i].end());
	  for(int j=0; j<yardSize[1]; j++)
	    {
	      maxColHeight = *max_element(lawnCols[j].begin(), lawnCols[j].end());
	      if(maxRowHeight > lawn[i][j] && maxColHeight > lawn[i][j])
		{
		  status =-1;
		  break;
		}
	    }
	}

      //Output Results
      if(status==0)
	cout << output1 << c << outputPass << endl;
      if(status<0)
	cout << output1 << c << outputFail << endl;

      //reset variables
      status = 0;
      lawn.clear();
      lawnCols.clear();
    }
}


// //for testing input
// cout << lawnCols.size() << " " << lawnCols[0].size() << endl;	  
// for(int N=0; N<yardSize[0]; N++)
// 	{
// 	  for(int M=0; M<yardSize[1]; M++)
// 	    cout << lawnCols[M][N] << " ";
// 	  cout << endl;
// 	}
