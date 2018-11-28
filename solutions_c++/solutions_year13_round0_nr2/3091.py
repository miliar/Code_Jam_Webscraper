#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <numeric>
using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define IREP(it,array) for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it)
#define PREP(it,array) for(vector<P>::iterator it=array.begin(); it!=array.end(); ++it)
#define SREP(it,array) for(vector<string>::iterator it=array.begin(); it!=array.end(); ++it)

#define MP       make_pair
#define PB       push_back
#define ALL(x)   (x).begin(),(x).end()

const int INF = 1<<29;
const double EPS = 1e-9;
double zero(double d){
  return d < EPS ? 0.0 : d;
}

typedef long long LL;
typedef pair<int,int> P;


int main()
{
  cout.setf(ios::fixed, ios::floatfield);
  cout.precision(7);


  int T;
  cin >> T;
  REP(targetNum,T){
    int N,M;
    cin>>N>>M;

    int height[N][M];
    int maxRow[N], maxCol[M];
    memset(maxRow, 0, sizeof(maxRow));
    memset(maxCol, 0, sizeof(maxCol));

    REP(i,N){
      REP(j,M){
	int a;
	cin>>a;
	height[i][j] = a;
	maxRow[i] = max(maxRow[i], a);
	maxCol[j] = max(maxCol[j], a);
      }
    }

    int init[N][M];
    REP(i,N){
      fill( init[i], init[i]+M, 100 );
    }

    bool isSuccess=true;
    REP(i,N){
      REP(j,M){
	if( init[i][j] > maxRow[i] )
	  init[i][j] = maxRow[i];
	if( init[i][j] > maxCol[j] )
	  init[i][j] = maxCol[j];

	if( init[i][j] != height[i][j] ){
	  isSuccess = false;
	  break;
	}	 
      }

      if( !isSuccess )
	break;
    }


    cout << "Case #" << targetNum+1 << ": " ;
    if(isSuccess)  cout << "YES";
    else cout << "NO";
    cout << endl;
  }



  return 0;
}
