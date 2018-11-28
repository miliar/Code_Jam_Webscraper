#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#define FOR(i,a,b) for (int i = a; i <= b; i++)
#define FORN(i,N) for (int i = 0; i < N; i++)
#define FORD(i,a,b) for (int i = a; i >= b; i--)


using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

bool temp[101];
void flip(int l, int r) {
  for(;l<=r;l++,r--) {
    bool ll = !temp[l];
    bool rr = !temp[r];
    temp[l] = rr;
    temp[r] = ll;
  }
}



int main() {
  int T;
  scanf("%d",&T);

  FOR(c,1,T) {
    string str;
    cin >> str;

    int Sl = str.size();

    FORN(i,Sl)
      if(str[i] == '-') temp[i] = false;
      else temp[i] = true;

    int leftmostZero = Sl-1;
    int count = 0;
    while(leftmostZero >= 0) {
      leftmostZero = Sl-1;

      while(temp[leftmostZero] && leftmostZero >= 0)
        leftmostZero--;

      if(leftmostZero < 0) {
        cout << "Case #" << c <<": " << count << endl;
        break;
      }
      

      if(temp[0] == true) {
       int rightContigOne = 0;
       for(rightContigOne = 0; temp[rightContigOne]; rightContigOne++);
       flip(0,rightContigOne-1);
      }
      else {
        flip(0,leftmostZero);
      }
      /*FORN(i,Sl) {
        if(temp[i]) printf("+");
        else printf("-");
      }
      printf("\n");
      */
      
      count++;
    }

  }
  
  return 0;
}
