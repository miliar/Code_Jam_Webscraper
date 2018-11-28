#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include "math.h"
#include <cstdlib>
#include <ctime>
using namespace std;

#define PB          push_back
#define MP          make_pair
#define S           size()
#define x           first
#define y           second
#define min(a,b)  (a<b? a:b)
#define max(a,b)  (a>b? a:b)
// #define log2(a)   log(a) / log(2.0)
typedef long long   LL;

std::vector<int> a;
std::vector<int>::iterator it;

int main(){
  ofstream myfile;
  myfile.open ("output.txt");
  int cases;
  cin >> cases;
  for (int c = 0; c < cases; ++c)
  {
    int vp, vq, v;
    char x;
    bool p = true;
    cin >> vp >> x >> vq;
    // cout << ((double) log2(vq) - (int) log2(vq)) << " " << (double) log2(vq) << " " << floor(log2(vq)) << endl;
    if(vq>2 && ((log2(vq) - floor(log2(vq))) != 0 || log2(vq) - ceil(log2(vq)) != 0)){
      myfile << "Case #" << c+1 << ": " << "impossible" << endl;
      continue;
    }
    v = vp*2;
    int ancestor = 0;
    double n = (double) ceil(v/2)/vq;
    while(n < 1){
      n *= 2;
      ancestor++;
    }
    myfile << "Case #" << c+1 << ": " << ancestor << endl;
  }
}