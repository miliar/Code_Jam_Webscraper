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

long long ggd(long long a, long long b) {
  if(b==0) return a;
  return ggd(b, a%b);  
}

bool power2(long long a) {
  return !(a&(a-1));
}

int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1;_case<=_cases;_case++) {
    printf("Case #%d: ", _case);
    long long P,Q;
    scanf("%lld/%lld", &P,&Q);
    long long g = ggd(P,Q);
    P/=g; Q/=g; 
    if(!power2(Q)) printf("impossible\n");
    else {
      for(k=0;k<45;k++) {
        if(P>=Q) {
          printf("%d\n", k);
          break;
        }
        P*=2;
         
      }
    }
  }

  return 0;
}
