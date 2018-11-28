#include <fstream>
#include <iostream>
using std::endl;
using std::cout;
#include <stdlib.h>
#include <string>
using std::string;
#include <vector>
using std::vector;
#include <map>
using std::map;

#include <utility>
using std::pair;

#include <boost/format.hpp>
using boost::format;              // format( "%1% %2%" % var1 % var2 )
#include <boost/foreach.hpp>      // BOOST_FOREACH( itemtype i, container)include <boost/lexical_cast.hpp> // lexical_cast<class_to> var
#include <boost/lexical_cast.hpp>
using boost::lexical_cast;

std::ofstream gLogger("./log");
//std::ostream logger2( stdout );

/*void SortedInsertInt( vector<int> &v, const int &i) {
  for (vector<int>::iterator itr=v.begin(); itr!=v.end(); ++itr){
    if (i < *itr) {
      v.insert(itr,i);
      return;
    }
  }  
  v.push_back(i);
}
*/

class Lottery {
public:
  Lottery( const char * filename ) : mInFile(filename)  {
    gLogger << "Lottery contructed with: " << filename << endl;
  }
  void Load() {
    mInFile >> mNumTestCases;
    gLogger << "Number of testcases: " << mNumTestCases << endl;

    int tmpItem;
    for (int testCaseIdx=1; testCaseIdx <= mNumTestCases; ++testCaseIdx) {
       gLogger << " Loading testcase: " << testCaseIdx << endl;
       mInFile >> mOldRndMax >> mNewRngMax >> mBuyMax;
       gLogger << "Old rng is: " << mOldRndMax << "\t\tnew rng max is: " << mNewRngMax 
               << "\t\tbuy list max: " << mBuyMax;
       cout << "Case #" << testCaseIdx << ": " << this->SolveCurrentProblem() << endl;
    }
  }
  
  std::string SolveCurrentProblem() {
    int winning=0;
    
    //generat pairs
    vector< pair<int,int> > generatorPairs;
    for ( int oldrng=0; oldrng<mOldRndMax; ++oldrng) {
      for (int newrng=0; newrng< mNewRngMax; ++newrng) {
        generatorPairs.push_back( pair<int,int>(oldrng,newrng) );
      }
    }
    
    vector< int > possible_answers;
    gLogger << endl;
    for ( auto itr = generatorPairs.begin(); itr != generatorPairs.end(); ++itr) {
      gLogger << "<" << itr->first << "," << itr->second << ">";
      int answer = itr->first & itr->second;
      //possible_answers.push_back( answer );
      gLogger << ": " << answer << endl;
      if  (mBuyMax > answer) winning++;
    }
    
    
    return lexical_cast<string>(winning);
  }
  
private:
  Lottery();
  std::ifstream mInFile;
  int mNumTestCases;
  int mOldRndMax, mNewRngMax, mBuyMax;
};

void cleanup() {
  gLogger.close();
}

int main(int argc, char ** argv) {
  if (argc < 2) {
    std::cerr << "No file given\n";
    return 1;
  } else {
    atexit(&cleanup);
    Lottery problem(argv[1]);    
    problem.Load();
  }
  return 0;
}