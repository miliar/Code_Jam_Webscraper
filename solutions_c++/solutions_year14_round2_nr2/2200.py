#include <cmath>
#include <queue>
#include <vector>
#include <queue>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <iomanip>   
#include <iostream>  
#include <sstream>  // istringstream buffer(myString);
#include <stack>
#include <set>
#include <algorithm>
#include <cstring>
#include <limits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main() {
  freopen("B-small-attempt0.in","r",stdin);
  //freopen("in","r",stdin);
  freopen("B-small.out","w",stdout);
  int TC, CASE=1;
  scanf("%d", &TC);
  while(TC--) {
    int A,B,K;
    cin >> A >> B >> K;
    int cnt=0;
    for(int i=0;i<A;i++) {
      for(int j=0;j<B;j++) {
        for(int k=0;k<K;k++) {
          if ((i & j) == k) {
            cnt++;
          }
        }
      }
    }

    printf("Case #%d: %d\n", CASE++, cnt);
  }
}
