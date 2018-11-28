#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef unsigned int ui;

#define FOR(i,a,b) for(auto i = (a); i < (b); ++i)
#define FORe(i,a,b) for(auto i = (a); i <= (b); ++i)
#define FORrev(i,a,b) for(auto i = (b); i >= (a); --i)
#define REP(i,a) FOR(i,0,a)
#define REP1(i,a) FOR(i,1,a)

#define ALL(it) (it).begin(),(it).end()
#define EACH(it, i) for(auto& i : it)

#define SCAN(i,f) scanf("%" #f " ",i)
#define GET(t,x,f) t x; SCAN(&x, f)
#define GETi(x) GET(int,x,d)
#define GETl(x) GET(ll,x,lld)
#define GETc(x) GET(char,x,c)
#define GETf(x) GET(float,x,f)
#define GETd(x) GET(double,x,lf)

#define pb push_back
#define mp make_pair
#define itr iterator
#define sz size()
#define A first
#define B second

int main(int argc, char** argv){
  	GETi(cases);
  	REP(kase, cases){
  		printf("Case #%d: ", kase + 1);
  		ui sum = 0;
  		GETi(ma); GETi(mb); GETi(ca);
  		REP(i,ma){
  			REP(j,mb){
//  				cout << ma << " & " << mb << endl;
  				if((i & j) < ca) sum++;
  			}
  		}
  		printf("%d\n", sum);
  	}

	return EXIT_SUCCESS;
}
