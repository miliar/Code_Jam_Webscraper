#include <vector>
#include <list>
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

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int s;
    scanf("%d",&s);
    string a;
    cin >> a;
    int c=0,f=0;
    for(int i=0;i<=s;i++)
    {
               if(c<i && (a[i]-'0')!=0)
               {
                      
                      f = f + (i-c);
                      c = c + (i-c);
                      c = c + (a[i]-'0');       
               }
               else
               {
                   c = c + (a[i]-'0');
               }     
            
            
    }
    
    printf("%d\n",f);
    }
  //system("PAUSE");
  return 0;
}
