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
const int inf = 1<<29;
const int maxn = 10000;
int used[maxn];
void Init() {
     memset(used, -1, sizeof(used));
     for(int i =1 ; i*i < maxn; i++) {
         used[i*i] = i;
     }
}
bool judge(int now) {
     vector<int> li;
     while(now>0) {
         li.push_back(now%10);
         now/=10;
     }
     int l = 0 , r = li.size()-1;
     while(l<r){
          if(li[l] != li[r])
              return false;
          l++;r--;
     }
     return true;
}
int main() {
    freopen("C:/Users/wangkun/Downloads/C-small-attempt0.in", "r" , stdin);
    freopen( "D:/result.out",  "w",stdout); 
    int T ,a ,b ,cas, sum;
    cin >> T;
    Init();
    cas = 0;
    while(T--) {
         cas ++;
         cin >> a >>b;
         sum = 0;
         for(int i = a ;i <= b; i++) {
              if((used[i] != -1) && judge(i) && judge(used[i])) {
                  sum++;
              } 
         }
         cout << "Case #"<<cas <<": " << sum << endl;
    }
    return 0;
}
