#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <stack>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;
double const PI = acos(-1.0);
double const EPS = 1e-9;
string const FILE_NAME = "A-large";
char S[1010];

int main(){
  freopen((FILE_NAME + string(".in")).c_str(),"r",stdin);
  freopen((FILE_NAME + string(".out")).c_str(),"w",stdout);
  int t;
  int s_max;
  int invite;
  int acu;
  int diff;
  scanf("%d",&t);
  for(int test_case = 1 ; test_case<=t ; test_case++){
  	scanf("%d %s",&s_max,S);
  	invite = 0;
  	acu = 0;
  	for(int i=0 ; i<=s_max ; i++){
  		diff = i - acu;
  		if(diff>0) {
  			invite += diff;
  			acu += diff;
  		}
  		acu += S[i] - '0';
  	}
  	printf("Case #%d: %d\n",test_case,invite);
  }
  return 0;
}