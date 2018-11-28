#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>
#include <complex>
#include <cmath>
#include <cstdio>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vec;
typedef vector<vec> mat;
static const double EPS = 1e-6;
static const double PI = acos(-1.0);

int main(){
  int T;
  cin >> T;
  long double C,F,X;
  long double create_num;
  long double time;
  for(int t=1;t<=T;++t){
    cin >> C >> F >> X;
    time = 0.0;
    create_num = 2.0;

    if( C >= X){ printf("Case #%d: %.7Lf\n",t,X/create_num);continue; }
    while( X > 0 && X >= C){
      //cout << create_num << " : " << X << " : " << time << endl;
      if( X/create_num  < ( C / create_num + X / (create_num + F) ) ){ break; }

      time += C / create_num;
      create_num += F;
    }
    if(X > 0)
      time += X / create_num;
    printf("Case #%d: %.7Lf\n",t,time);
  }
  return 0;
}
