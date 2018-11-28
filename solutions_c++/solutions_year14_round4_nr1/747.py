#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1;_case<=_cases;_case++) {
    int x, n;
    scanf("%d %d", &n, &x);
    vi s;
    for(i=0;i<n;i++) {
      scanf("%d",&k);
      s.pb(k); s.pb(0);
    }
    printf("Case #%d: ", _case);
    sort(s.begin(),s.end());
    reverse(s.begin(), s.end());
    for (k=(n+1)/2;k<=n;k++) {
      bool kan=true;
      for(i=0;i<k;i++) {
        if(s[i]+s[2*k-1-i]>x) {kan=false; break; }
      }
      if(kan) {
        printf("%d\n", k);
        break;
      }
    }

  }


  return 0;
}
