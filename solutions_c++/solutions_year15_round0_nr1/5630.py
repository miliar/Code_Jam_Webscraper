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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt,j,jj,fr=0;
  scanf("%d ", &tt);
  for(int i=0; i<tt ;++i){
    fr =0;
    int max,tmp,tot=0;
    scanf("%d ", &max);
    for(j=0;j<=max;j++){
      scanf("%1d", &tmp);
      if(j>tot){
        fr += (j-tot);
        tot+=(j-tot) + tmp;
      }
      else tot+=tmp;
    }
    cout<<"Case #"<<i+1<<": "<<fr<<endl;
  }
  return 0;
}
