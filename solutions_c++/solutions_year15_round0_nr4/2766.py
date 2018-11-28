#include <iostream>
#include <string.h>
#include <stdio.h>
#include <set>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <algorithm>
#include <map>
#include <streambuf>
#include <sstream>
#include <queue>
#include <iomanip>
#define ll long long
#define INF 1e9
#define PI acos(-1.0)
using namespace std;

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
int T;
cin >> T;
int tst = 1;
while(T--)
{
   bool g = 1;
   int x,r,c;
   cin >> x >> r >> c;
   if(r > c) swap(r,c);
   if(r == 1 && c == 1) {
    if(x > 1) g = 0;
   }
   if(r == 1 && c == 2) {
    if(x > 2) g = 0;
   }
   if(r == 1 && c == 3) {
    if(x > 1) g = 0;
   }
   if(r == 1 && c == 4)
   {
       if(x > 2) g = 0;
   }
   if(r == 2 && c == 2) {
    if(x > 2) g = 0;
   }
   if(r == 2 && c == 3) {
    if(x == 4) g = 0;
   }
   if(r == 2 && c == 4) {
    if(x > 2) g = 0;
   }
   if(r == 3 && c == 3) {
    if(x % 2 == 0) g = 0;
   }
   if(r == 3 && c == 4) {
   }
   if(r == 4 && c == 4) {
    if(x == 3) g = 0;
   }
   (g)?printf("Case #%d: GABRIEL\n",tst++):printf("Case #%d: RICHARD\n",tst++);

}
return 0;
}

