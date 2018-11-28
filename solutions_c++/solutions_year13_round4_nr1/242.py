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

struct Trip {
  int st;
  int fin;
};

static const long long MOD = 1000002013;

long long cost( long long N, long long Dis ) {
  return (N * Dis - Dis * (Dis - 1) / 2) % MOD;
}


void solveTest()
{
  int N, M;
  in >> N >> M;
  vector<Trip> a(M);
  long long total1 = 0;
  long long total2 = 0;
  vector<int> cc1(M), cc2(M);
  for( int i = 0; i < M; i++ ) {
    in >> a[i].st >> a[i].fin >> cc1[i];
    cc2[i] = cc1[i];
    total1 = (total1 + cost( N, a[i].fin - a[i].st ) * cc1[i]) % MOD;
  }
  cerr << total1 << endl;
  for( int i = 0; i < 2 * M; i++ ) {
    int best = 2000000000;
    int ind1 = 0;
    int ind2 = 0;
    for( int j = 0; j < M; j++ ) {
      if( cc1[j] == 0 ) continue;
      for( int k = 0; k < M; k++ ) {
	if( cc2[k] == 0 ) continue;
	if( a[j].st > a[k].fin ) continue;
	int tmp = a[k].fin - a[j].st;
	if( tmp < best ) {
	  best = tmp;
	  ind1 = j;
	  ind2 = k;
	}
      }
    }
    if( best == 2000000000 ) {
      break;
    }
    int tmp = std::min(cc1[ind1], cc2[ind2]);
    cc1[ind1] -= tmp;
    cc2[ind2] -= tmp;
    total2 = (total2 + cost( N, best ) * tmp) % MOD;
  }
  cerr << total2 << endl;
  out << ( total1 % MOD - total2 % MOD + MOD) % MOD << "\n";
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
