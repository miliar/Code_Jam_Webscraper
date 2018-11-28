#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

int a[1010];

int run() {
  int n;
  scanf("%d", &n);
  for(int i=0;i<n;++i) scanf("%d", a+i);
  int ans = *max_element(a,a+n);
  for(int i=1;i<ans;++i){
    int cur=i;
    for(int j=0;j<n;++j){
      if(a[j] > i) {
        cur += ( a[j] - 1 ) / i;
      }
    }
    ans =min(ans,cur);
  }
  return ans;
}

int main() {
  
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  
  int test;
  scanf("%d", &test);
  for(int no=1;no<=test;++no)
    cout << "Case #"<<no<<": "<<run()<<endl;
}
