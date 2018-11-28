#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
using namespace std;

int main()
{
	int T;
  
  cin >> T;
  
  for (int t = 1; t <= T; ++t) {
    int S;
    string X;
    
    cin >> S >> X;
    int shy = 0;
    int need = 0;
    for (int i = 0; i <= S; ++i) {
      if (X[i] == '0') continue;
      if (shy < i) {
        need += i - shy;
        shy = i;
      }
      shy += X[i] - '0';
    }
    printf("Case #%d: %d\n", t, need);
  }
	
	return 0;
}
