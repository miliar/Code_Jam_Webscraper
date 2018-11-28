//
//  15d1.cpp
//  
//
//  Created by Ritish Goyal on 11/04/15.
//
//

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define rep(i, n) for(int i=0; i<n; i++)

int main() {
    int test; cin>> test;
    int ans = 0;
    rep(z, test) {
      int x, r, c;
      scanf("%d %d %d\n", &x, &r, &c);
      if(x >=7) {
	ans = 1;
      }
      else if(r < (x+1)/2 || c < (x+1)/2 || (r < x && c < x)) {
	ans = 1;
      }
      else if((r*c)%x != 0) {
	ans = 1;
      }
      else if(x==4 && r*c == 8) {
	ans = 1;
      }
      else if(x==6 && r*c == 18) {
	ans = 1;
      }
      else {
	ans = 0;
      }
      if(ans == 1) {
	printf("Case #%d: RICHARD\n", z+1);
      }
      else {
	printf("Case #%d: GABRIEL\n", z+1);
      }
    }
}
