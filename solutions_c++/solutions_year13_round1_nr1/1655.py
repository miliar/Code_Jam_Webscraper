/* Template Creator : Timothy Leung */
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>
#include <sstream>
#include <stack>
#include <string.h>
#include <cstdlib>
#include <iterator>

/* Short Cut */
#define rep(i,n) for(int i=0; i<n; i++)
#define rrep(i,n) for(int i=1; i<=n; i++)
#define drep(i,n) for(int i=n-1; i>=0; i--)
#define maxs(x,y) x = max(x,y);
#define mins(x,y) x = min(x,y);
#define pb push_back
#define PI 3.1415926536

using namespace std;

typedef long long int ll;

int main(){
  /* code start here */
  int num_case;
  long long int r,t;
  cin >> num_case;
  for(int num=1; num<=num_case; num++){
      cin >> r >> t ;
      int k=0;
      long int count = 0;
      while(t>0){
	  t -= (2*r+2*k+1);
	  if(t>=0) count++;
	  k+=2;
      }
      cout << "Case #" << num << ": "<< count << endl;
  }
  return 0;
}

