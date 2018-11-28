
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <sstream>
#include <cmath>

using namespace std;


#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fi(n) forn(i,n)
#define fj(n) forn(j,n)
#define fk(n) forn(k,n)
#define sz size()
#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define last(a) int(a.size() - 1)

int case_number = 0;
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define fs first
#define sc second


typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;


const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ll inf64 = ((ll)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;


int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }



int main( )
{
	
	int T;
  cin >> T;

  while (T--){

    long long r, n;
    cin >> r >> n;
    long long  sol = 0;
    do{
      n = n - (r+1)*(r+1) + r*r;
      r+=2;
      if( n < 0) break;
      sol++;
    }while(true);

    gout << sol << endl;


  }
	
	
	return 0;
}
