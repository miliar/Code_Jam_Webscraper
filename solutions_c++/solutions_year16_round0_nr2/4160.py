//Javier Guzmán
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int t, ans;
char str[101];
int main(){
   scanf("%d", &t);
   for(int test=1; test<=t; test++){
      ans=0;
      scanf("%s", &str);
      char c = str[0];
      for(int i=0; i<strlen(str); i++){
         if(str[i]!=c){
            ans++;
            c=str[i];
         }
      }
      if(c=='-') ans++;
      printf("Case #%d: %lld\n", test, ans);
   }
   return 0;
}
