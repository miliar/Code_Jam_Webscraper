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
  int i=0,j=0,k=0;\
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1; _case<=_cases; _case++) {
    vi tel = vi(17,0);
    int r; 
    for(k=0;k<2;k++) {
      scanf("%d",&r);
      for(j=0;j<4;j++) for(i=0;i<4;i++) {
        int v; scanf("%d", &v);
        if(j==r-1) tel[v]++;
      }
    }
    int ant=-1;
    int aantal=0;
    for(k=1;k<=16;k++) 
      if(tel[k]==2) {ant=k; aantal++;}
    printf("Case #%d: ", _case);
    if(aantal==0) printf("Volunteer cheated!\n");
    else if(aantal>1) printf("Bad magician!\n");
    else printf("%d\n",ant);
  }


  return 0;
}
