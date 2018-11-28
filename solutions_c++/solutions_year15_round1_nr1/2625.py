#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <fstream>
#include <cassert>
#include <cstdlib>
using namespace std;

// Shortcuts for common data type
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef set<int> si;

int main(){
  FILE *fin = freopen("inputA", "r", stdin);
  assert( fin!=NULL );
  FILE *fout = freopen("outputA", "w", stdout);
  
  int cases;
  cin >> cases;
  
  for(int i = 1 ; i<=cases; i++){
    if(i != 1)
      cout << endl;
    cout << "Case #" << i << ": ";

    int intervals;
    cin >> intervals;
    
    int sum1=0;
    int maxdiff=0;
    int a[intervals];

    cin >> a[0];
    for(int j=1; j<intervals; j++){
      cin >> a[j];

      int diff = a[j-1]-a[j];

      sum1 = (diff>0) ? sum1 + diff : sum1;
      maxdiff = (diff > maxdiff) ? diff : maxdiff;
    }

    ll sum2=0;
    for(int j=0; j<intervals-1; j++){
      sum2 = (a[j]> maxdiff) ? sum2 + maxdiff: sum2+a[j];
    }
    
    cout << sum1 << " " << sum2;    
  }
  return 0;
}
