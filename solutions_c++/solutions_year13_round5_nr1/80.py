#include <stdio.h>
#include <vector>
#include <map>
#include <stdlib.h>
#include <string>
#include <set>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream in( "input.txt" );
ofstream out( "output.txt" );

void solveTest()
{
  long long money;
  vector<long long> a(37);
  int n;
  in >> money >> n;
  for( int i = 0; i < n; i++ ) {
    in >> a[i];
  }
  sort(a.begin(), a.end());
  double result = 0.0;
  for( int i = 1; i <= 36; i++ ) {
    long long min = a[i-1];
    long long max = 10000000000000LL;
    while( max - min > 1 ) {
      long long med = (max + min) / 2;
      long long total = 0;
      for( int j = 0; j < a.size(); j++ ) {
	if( j < i ) {
	  total += med - a[j];
	} else {
	  total += a[j] > med ? 0 : med - a[j] + 1;
	}
      }
      if( total > money ) {
	max = med;
      } else {
	min = med;
      }
    }
    long long total = 0;
    long long useful = 0;
    for( int j = 0; j < a.size(); j++ ) {
	if( j < i ) {
	  useful += min - a[j]; 
	  total += min - a[j];
	} else {
	  total += a[j] > min ? 0 : min - a[j] + 1;
	}
    }
    if( total > money ) {
      continue;
    }
    cerr << i << " " << min << " " << total << " " << useful << endl;
    double tmp = 36.0 / i * useful - total;
    if( tmp > result ) {
      result = tmp;
    }
  }
  out << setprecision(8) << result << "\n";
}

void run()
{
  int tn;
  in >> tn;
  for( int i = 1; i <= tn; i++ ) {
    out << "Case #" << i << ": ";
    solveTest();
  }
}

int main()
{
  run();
  return 0;
}
