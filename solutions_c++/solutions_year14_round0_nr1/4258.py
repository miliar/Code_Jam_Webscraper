#ifndef _MAGIC_TRICK_H_
#define _MAGIC_TRICK_H_

#include <fstream>
#include <string>

using namespace std;

class MagicTrick
{
  public:
    MagicTrick( ifstream& infile );
    ~MagicTrick();
    string algorithm(string first, string second );

  private:
    int _testcases;
    ofstream _outfile;
};

#endif
