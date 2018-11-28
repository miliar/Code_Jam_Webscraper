#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <fstream>
#include <complex>
#include <cassert>
#include <iostream>
#include <algorithm>
/*
//      Code By "SAEED EZZATI"
//      g++ A.cpp -o A.o && ./A.o in.in out.out 
*/
using namespace std;

#define pb push_back
#define mp make_pair
#define min(x,y) (x<y?x:y)
#define max(x,y) (x>y?x:y)

typedef long long LL;//10^19
typedef long double LD;//10^370
typedef vector<int> VI;
typedef vector<unsigned int> VUI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define smallLine 100
#define largeLine 1000

//////////////////// Public Variables
int T; /// Number of Inputs
char* input_file;
char* output_file;
clock_t t;
/////////////////////////////////////////////////// Function
int function(const LL &r, const LL &t);
///////////////////////////////////////////////////
int main(int argc, char* argv[])
{
  if(argc<3){
    cout << "\n > ERROR: 'Usage: ./alienNumbers.o input_file output_file' " << endl;
    return -1;
  }
  
  input_file=argv[1];
  output_file=argv[2];
  cout.setf(ios::fixed);
  cout.precision(0);
  t = clock();
  /// Reading Input File
  ifstream in_file;
  in_file.open(input_file);
  /// Opening Output File
  ofstream out_file;
  out_file.setf(ios::fixed);
  out_file.precision(0);
  out_file.open(output_file, fstream::app);
  if(in_file.is_open()){
    cout << "\n\n > '" << input_file << "' opened correctly!" << endl;

    int lineN = 0; /// Line Number
    string line;
    LL r;
    LL t;
    while(!in_file.eof()){
      /// Reading First Line 
      if(lineN==0){
        getline(in_file, line);
        stringstream ss (line, stringstream::in | stringstream::out);
        for(int i=0; i< 1; ++i){//<<<<
          ss >> T;
        }
        cout << " > Number of Tests: " << T << endl;
        cout << " > Reading Data from: '" << input_file << "'" << endl;

      /// Reading DATA 
      }else if(lineN>0 && lineN<=T){// <<<<
        
        //cout << "\n" << lineN <<"  > IN: "; //<<<<
  
        /// Reading Words From Lines
        getline(in_file, line);
        stringstream ss1 (line, stringstream::in | stringstream::out);
        ss1 >> r >> t;

        /*CODE HERE*/
        
        /// Write to Output Vector
        if(out_file.is_open()){
          out_file << "Case #" << lineN << ": " << function(r,t) << endl;  
        }else{
          cout << " > Unable to open output file: " << output_file << endl;
          return -1;
        }
      cout << ".";
      }
      ++lineN;

      if(in_file.eof()){
        break;
      }

    }
    cout << "\n";     

  }else{
    cout << " > Unable to open input file: " << input_file << endl;
    return -1;
  }
  
  in_file.close(); 
  out_file.close();
  
  /// Timing Results
  t = clock() - t;
  cout << " > It took me " << t << " Clicks OR " << ((float)t)/(CLOCKS_PER_SEC) << " Seconds to Process Input File and Create the Output File!" << endl;
  cout << " > Bye" << endl; 
return 0;
}
//////////////////////////////////////////////////
int function(const LL &r, const LL &t)
{
  int x=0,i=0;
  LL q=t;
  while( q-(pow((double)(r+i+1),2.0)-pow((double)(r+i),2.0)) >= 0){
    ++x;
    q-=(pow((double)(r+i+1),2.0)-pow((double)(r+i),2.0));
    i+=2;
  }
return x;
}
//////////////////////////////////////////////////
