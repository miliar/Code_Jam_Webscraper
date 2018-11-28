/* 1352652 周宇星 数理强化班 */
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
using namespace std;

/*
int get(){
  char c;
  while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
  bool flag=(c=='-');
  if(flag) c=getchar();
  int x=0;
  while(c>='0'&&c<='9'){
      x=x*10+c-48;
      c=getchar();
  }
  return flag?-x:x;
}
void output(int x){
  if(x<0){
      putchar('-');
      x=-x;
  }
  int len=0,data[10];
  while(x){
      data[len++]=x%10;
      x/=10;
  }
  if(!len) data[len++]=0;
  while(len--) putchar(data[len]+48);116.5.12.148
  putchar('\n');
}*/


/*----------------------------------------------Thanks for viewing--------------------------------*/

void work(int m) {
    int ans = 0,nows = 0,smax;
    string reader;
    cin >> smax >> reader;
    for (int i = 0;i <= smax;i++) if ((reader[i] - '0') > 0){
        if (nows >= i) {
            nows += (reader[i] - '0');
        }else {
            ans += i - nows;
            nows = i + (reader[i] - '0');
        }
    }
    printf("Case #%d: %d\n",m,ans);
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int caset;
    cin >> caset;
    for (int t = 1; t <= caset;t++)
        work(t);
    return 0;
}
