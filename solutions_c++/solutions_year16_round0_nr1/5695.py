#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <cmath>
#include <sstream>
using namespace std;

int getLast(int num){
   unordered_set<int> dict;
   int max_iter = 200, this_num = num;
   for (int i = 1; i < max_iter; i++){
      this_num = num*i;
      int rest_num = this_num;
      while(rest_num > 0){
         dict.insert(rest_num % 10);
         rest_num = rest_num/10;
      }
      if (dict.size() == 10)
         return this_num;
   }
   return -1;
}

int main() {
    freopen("p1.input","r",stdin);//redirects standard input
    int n, num, ret=0;
    scanf("%d\n", &n);
    for(int i=0;i<n;i++){
        scanf("%d\n", &num);
        int last = getLast(num);
        if (last < 0)
         cout<< "Case #" << i+1 << ": INSOMNIA" << endl;
        else
         cout<< "Case #" << i+1 << ": " << last << endl;
    }
    return 0;
}
