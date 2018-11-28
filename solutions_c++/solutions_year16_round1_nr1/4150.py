#include <vector>
#include <list>
#include <string.h>
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
#define ll long long

using namespace std;

int main() {
 freopen("A-large (1).in", "r", stdin);
 freopen("A-large (1).out", "w", stdout);
  int tt;
  scanf("%d",&tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ",qq);
       char s[1005] ,ans[1005];
       scanf("%s",s);
       int k = strlen(s);
       string st = "";
       for(int i = 0 ; i < k ;i++){
           if( st + s[i] > s[i] + st )   st += s[i];
           else                          st = s[i] + st;
       }
       for(int i = 0 ; i < k ;i++){
       	  printf("%c",st[i]);
	   }
	   printf("\n");
    }
     return 0;
}
