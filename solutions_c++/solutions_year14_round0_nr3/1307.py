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

void printveld(vs veld) {
  if(sz(veld)==0) printf("Impossible\n");
  for(int j=0;j<sz(veld);j++)
    printf("%s\n",veld[j].c_str());
}

int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  int R, C, M, h, b;
  for(_case=1;_case<=_cases;_case++) {
    scanf("%d %d %d", &R, &C, &M);
    printf("Case #%d:\n", _case);

    vs veld;
    if(M==R*C-1) { //Just one empty spot
      veld = vs(R, string(C, '*'));
      veld[0][0]='c';
    } else if(R==1) { //Single row
      veld = vs(1, "c" + string(R*C - M - 1, '.') + string(M, '*'));
    } else if(C==1) { //Single column
      veld = vs(R, string(1, '*'));
      veld[0][0]='c';
      for(i=1;i<R*C-M;i++) veld[i][0]='.';
    } else { //Other cases
      for(h=2;h<=R;h++) for(b=2;b<=C;b++) {
        if (sz(veld)==0 && h*b>=R*C-M && R*C-M>=2*b+2*h-4) {
          veld = vs(R, string(C, '*'));
          int rest=R*C-M-(2*b+2*h-4);
          for(j=0;j<h;j++)for(i=0;i<b;i++) if(j<2||i<2) veld[j][i]='.';
          veld[0][0]='c';
          for(j=2;j<h;j++)for(i=2;i<b;i++) if(rest>0) {rest--; veld[j][i]='.';}
        }
      }
    }
    printveld(veld);
  }
  return 0;
}
