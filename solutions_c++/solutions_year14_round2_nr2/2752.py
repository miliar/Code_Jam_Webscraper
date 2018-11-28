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
#include <cstdlib>
#include <ctime>
using namespace std;

#define PB          push_back
#define MP          make_pair
#define S           size()
#define x           first
#define y           second
typedef long long   LL;

std::vector<int> a;
std::vector<int>::iterator it;

int main(){
  ofstream myfile;
  myfile.open ("outputB.txt");
  int cases;
  cin >> cases;
  for (int c = 0; c < cases; ++c)
  {
    int A, B, K, result=0;
    cin >> A >> B >> K;
    for (int i = 0; i < A; ++i)
    {
      for (int j = 0; j < B; ++j)
      {
        if ((i&j) < K)
        {
          result++;
        }
      }
    }
    myfile << "Case #" << c+1 << ": " << result << endl;
  }
}
