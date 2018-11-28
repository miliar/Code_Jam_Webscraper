#include<iostream>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<complex>
#include<map>
#include<list>
#include<deque>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
using namespace std;

int log2(long long x){
  int res = 0;
  for(int i=0;i<60;i++){
    if((x>>i)&1LL)res = i;
  }
  return res;
}

int main(){
  int testcase;
  int ans;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    long long n,p;
    cin >> n >> p;
    long long N = 1LL<<n;

    long long l = 0,r = N;
    while(r-l>1){
      long long mid = (l+r)/2;
      int pop = log2(mid+1);
      if(N-(1LL<<(n-pop))+1<=p)l = mid;
      else r = mid;
    }
    long long res1 = l;

    l = 0, r = N;
    while(r-l>1){
      long long mid = (l+r)/2;
      int pop = log2(N-mid);
      if((1LL<<(n-pop))<=p)l = mid;
      else r = mid;
    }
    long long res2 = l;

    cout << "Case #" << casenum << ": ";
    cout << res1 << " " << res2 << endl;
  }
}
