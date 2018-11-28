/*************************************************************************
    > File Name: c.cpp
    > Author: implus
    > Mail: 674592809@qq.com
    > Created Time: 六  4/12 12:29:00 2014
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define ls (rt<<1)
#define rs (rt<<1|1)
#define lson l,m,ls
#define rson m+1,r,rs
int T, icase = 1, n;
int gao(vector<double> a, vector<double> b){
  sort(a.begin(), a.end(), greater<double>());
  sort(b.begin(), b.end(), greater<double>());

  int ans = 0;
  //for(int i = 0; i < a.size(); i++) cerr<<a[i]<<" ";cerr<<endl;
  //for(int i = 0; i < a.size(); i++) cerr<<b[i]<<" ";cerr<<endl;
  int pi = 0, pa = a.size() - 1, pb = 0;
  while(pb < b.size()){
    if(a[pi] < b[pb]){
      ans += a[pa--] > b[pb];
    }else{
      ans++;
      pi++;
    }
    pb++;
  }
  return ans;
}
int main(){
  scanf("%d", &T);
  while(T--){
    scanf("%d", &n);
    vector<double> a(n), b(n);
    for(int i = 0; i < n; i++) scanf("%lf", &a[i]);
    for(int i = 0; i < n; i++) scanf("%lf", &b[i]);
    printf("Case #%d: %d %d\n", icase++, gao(a, b), n - gao(b, a));
  }
  return 0;
}
