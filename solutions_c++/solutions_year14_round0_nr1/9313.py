//magic.cpp

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int main(int argc, char** args)
{
  if (argc < 2)  {cout << "No arg." << endl; return 1;}

  ifstream infile(args[1], ifstream::in);
  ofstream outfile(strcat(args[1], ".out"), ofstream::out);

  int totalCases;
  infile >> totalCases;
  for (int i=0; i < totalCases; i++)
  {
    outfile << "Case #" << i+1 << ": ";
    int row1, row2;
    infile >> row1;
    
    int d;
    for (int j=0; j < row1-1; j++)
    {
      infile >> d;
      infile >> d;
      infile >> d;
      infile >> d;
    }
    vector<int> row1row(4);
    infile >> row1row[0];
    infile >> row1row[1];
    infile >> row1row[2];
    infile >> row1row[3];

    for (int j=row1; j < 4; j++)
    {
      infile >> d;
      infile >> d;
      infile >> d;
      infile >> d;
    }

    infile >> row2;
    
    for (int j=0; j < row2-1; j++)
    {
      infile >> d;
      infile >> d;
      infile >> d;
      infile >> d;
    }
    vector<int> row2row(4);
    infile >> row2row[0];
    infile >> row2row[1];
    infile >> row2row[2];
    infile >> row2row[3];

    for (int j=row2; j < 4; j++)
    {
      infile >> d;
      infile >> d;
      infile >> d;
      infile >> d;
    }
    
    //now just find the intersection
    sort(row1row.begin(), row1row.end());
    sort(row2row.begin(), row2row.end());
    vector<int> inters(4);
    vector<int>::iterator it = set_intersection(row1row.begin(), row1row.end(), row2row.begin(), row2row.end(), inters.begin());
    inters.resize(it - inters.begin());
    
    //3 cases
    if (inters.size() == 0)
    {
      //no solution
      outfile << "Volunteer cheated!";
    }
    else if (inters.size() == 1)
    {
      //unique solution
      outfile << inters[0];
    }
    else
    {
      //more than one solution
      outfile << "Bad magician!";
    }
    outfile << endl;
  }
  
}