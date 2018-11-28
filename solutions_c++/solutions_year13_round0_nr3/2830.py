#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> base;
vector<long long> fair_square;

bool isPal(long long p) {
    vector<char> digits;
    while( p>0 ) {
        long long t = p/10;
        digits.push_back(p-t*10);
        p = t;
    }
    vector<char>::iterator forward = digits.begin();
    vector<char>::reverse_iterator reverse = digits.rbegin();
    for( int i=0;i<digits.size()/2+1;i++) {
        if( *forward != *reverse ) {
            return false;
        }
        forward++;
        reverse++;
    }
    return true;
}

long long pal(long long i, long long t) {
    long long pal = i;
    while( t>0 ) {
        long long by10 = t/10;
        pal = pal * 10 + (t-by10*10);
        t = by10;
    }
    if( !isPal(pal)) {
        printf("What!");
    }
    return pal;
}

void accumulateFaS(long long p) {
    long long fas = p*p;
    if( isPal(fas) ) {
        base.push_back(p);
        fair_square.push_back(fas);
    }

}



void compute() {

  for(long long i=1;i<30000;i++) {
    accumulateFaS(pal(i,i/10));
    accumulateFaS(pal(i,i));
  }
  sort(base.begin(),base.end());
  sort(fair_square.begin(),fair_square.end());
}

int main(int argc, const char* argv[]) {
  compute();
  ifstream infile("/Users/mseritan/Downloads/one.in");
  ofstream outfile("/Users/mseritan/Downloads/one.out");
  int tests=0;
  string line;
  getline(infile,line);
  stringstream(line) >> tests;
  printf("tests %d\n",tests);
  for( int t=1;t<=tests;t++) {
    int low, high;
    getline(infile,line);

    stringstream(line) >> low >> high;
    int count = 0;
    for( vector<long long>::iterator v = fair_square.begin(); v!=fair_square.end();++v) {
        if(*v >= low && *v <= high) {
            count++;
        }
    }
    outfile << "Case #" << t << ": "<<  count << endl;
  }
  return 0;
}
