#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<climits>


#define FOR(i,a,b) for(int i=int(a);i<int(b);i++)
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();it++)
#define SQ(x) (x)*(x)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;

unsigned long long n, rad, paint;

int k = 0;

double getArea(unsigned long long x){
  double a = (1+x);
  double b = (1+2*x+2*rad);
  return a*b;
}

unsigned long long findcircle(unsigned long long a){
  unsigned long long lastGuess = a-1;
  unsigned long long guess;

  for(unsigned long long i = 1;;i*=2){
    guess = a+i;
    //printf("guess:%lld\n",guess);
    double curArea = getArea(guess);
    if(curArea>paint && getArea(guess-1)<=paint)
      return guess;

    if(curArea>paint)
      return findcircle(lastGuess);
    lastGuess = guess;
  }
}

int main(){
  cin >> n;
  for(int ccase = 1;ccase<=n;ccase++){
    cin >> rad >> paint;
    printf("Case #%d: %lld\n",ccase,findcircle(0));
  }
  return 0;
}
