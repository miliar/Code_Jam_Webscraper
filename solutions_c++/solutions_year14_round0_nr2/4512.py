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
#include <string>
#include <cstring>

using namespace std;

typedef int ttyp;
#define forz(n) for(int i=0;i<n;i++)
#define forzo(j,n) for(int j=0;j<n;j++)
#define MP make_pair
#define sz(v) v.size()
#define E9 1e-9

void doit(){
    double c, f, x, ret, r, tsp = 0;
    double ttac, ttax, nret;
    cin>>c>>f>>x;
    r = 2;
    ret = x/r;
    forz(10000000){
        ttac = c/r;
        ttax = tsp+x/r;
        if(ttax>ret+E9)
            break;
        ret = ttax;
        tsp+=ttac;
        r+=f;
    }
    printf("%0.8f\n",ret);

  return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
      cout<<"Case #"<<i<<": ";
      doit();
    }
    return 0;
}

