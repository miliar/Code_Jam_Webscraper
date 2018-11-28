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

class Repeater {
public:
  Repeater( const char * filename ) : mInFile(filename)  {
    gLogger << "Repeater contructed with: " << filename << endl;
  }
  void Load() {
    mInFile >> mNumTestCases;
    gLogger << "Number of testcases: " << mNumTestCases << endl;

    int numStings;
    string tmpString;
    for (int testCaseIdx=1; testCaseIdx <= mNumTestCases; ++testCaseIdx) {
       gLogger << " Loading testcase: " << testCaseIdx << endl;
       mInFile >> numStings;
       mS.clear();
       /*for (int idx=0; idx<numStings; ++idx) {
         mInFile >> tmpString;
         mS.push_back( tmpString );
       }       
       
       gLogger << endl;
       BOOST_FOREACH( string s, mS ) {
         gLogger << "String: " << s << endl;
       }*/
       mInFile >> mOne;
       mInFile >> mTwo;
       gLogger << "\nLoading strings: " << mOne << ", " << mTwo;
       
       cout << "Case #" << testCaseIdx << ": " << this->SolveCurrentProblem() << endl;
    }
  }
  
  
  void Updateminlen() {
    mMinLen = ( mOne.length() < mTwo.length() ) ? mOne.length() : mTwo.length();
  }
  
  std::string SolveCurrentProblem() {
    //vector<string> tmpS = mS;
    int numchanges=0;
    
    Updateminlen();
    int idx =0 ;
    for ( ; idx <mMinLen; ++idx) {
      gLogger << "\nTesting idx: " << idx << "\t" << mOne << ", " << mTwo;;
      if ( mOne[idx] != mTwo[idx] ){
        gLogger << endl << mOne[idx] << "!=" << mTwo[idx];
        //Reduce first one?
        if ( idx>0 && mOne[idx-1] == mOne[idx]) { 
          mOne.erase( idx,1);
          numchanges++;
          gLogger << " Removed one: " <<  idx << endl;
          --idx;
          continue;
        }
        
        if ( idx>0 && mTwo[idx-1] == mTwo[idx]) { 
          mTwo.erase( idx,1);
          numchanges++;
          gLogger << " Removed two: " <<  idx << endl;
          --idx;
          continue;
          
        }
        return "Fegla Won";
      }
    }
     
      while (mOne.length() < mTwo.length()) {
        if (mTwo[mTwo.length() -1] ==  mTwo[mTwo.length() -2] ) {
          mTwo.erase(mTwo.length() -1,1);
          ++numchanges;
        } else
          break;
      }
      
      while (mTwo.length() < mOne.length()) {
        if (mOne[mTwo.length() -1] ==  mOne[mOne.length() -2]) {
          mOne.erase(mTwo.length() -1,1);
          ++numchanges;
        } else
          break;
      }
      
    if (mOne == mTwo) return lexical_cast<string>(numchanges);
    return "Fegla Won";
  }

private:
  Repeater();
  std::ifstream mInFile;
  int mNumTestCases;
  vector<string> mS;
  string mOne;
  string mTwo;
  int mMinLen;
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
    Repeater problem(argv[1]);    
    problem.Load();
  }
  return 0;
}