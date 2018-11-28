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

int n,m;
int o[1000],e[1000],p[1000];
int pop[1000];

int main(){
  int testcase;
  int ans;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    cin >> n >> m;
    for(int i=1;i<=n;i++)pop[i] = 0;

    long long sum = 0;
    for(int i=0;i<m;i++){
      cin >> o[i] >> e[i] >> p[i];
      for(int j=o[i];j<e[i];j++){
	pop[j] += p[i];
	sum += p[i]*(n-(j-o[i]));
      }
    }

    long long ans = 0;
    bool f = true;
    while(f){
      f = false;
      for(int i=1;i<=n;i++){
	if(pop[i]){
	  int cnt = 0;
	  for(int j=i;j<=n;j++){
	    if(pop[j]){
	      pop[j]--;
	      cnt++;
	      ans += n+1-cnt;
	    }else break;
	  }
	  f = true;
	  break;
	}
      }
    }

    cout << "Case #" << casenum << ": ";
    cout << sum-ans << endl;
  }
}
