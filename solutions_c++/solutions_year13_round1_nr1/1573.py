#include<iostream>
#include<fstream>
#include<string>
using namespace std;

static string inFile = "A-small.in";
static string outFile = "A-small.out";

long long Solve(long long r, long long t);

int main()
{
  ifstream in(inFile);
  if(in) {
    int numTests;
    in>>numTests;
    int curTest = 1;
    ofstream out(outFile);
    while(curTest<=numTests)
    {
      long long r, t;
      in>>r>>t;
      out << "Case #" << curTest << ": " << Solve(r, t) << endl;
      ++curTest;
    }
    out.close();
  }
  in.close();
  return 0;
}

long long Solve(long long r, long long t)
{
  long long paintLeft = t;
  long long curRadius = r;
  long long numBlackRings = 0;
  long long needed  = r+r+1;
  do {
    ++numBlackRings;
    paintLeft -= (needed);
    needed += 4;
  }while(paintLeft >= needed);
  return numBlackRings;
}