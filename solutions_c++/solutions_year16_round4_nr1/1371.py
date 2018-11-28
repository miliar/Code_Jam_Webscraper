#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;
typedef pair<int,int> pII;
pair<pII, int> Win[13];
string ch[3] = {string("R"), string("S"), string("P")};
string dfs(int f, int n){
  if(n == 0) return ch[f];
  else{
    string a = dfs(f, n-1);
    string b = dfs((f+1)%3, n-1);
    if(a < b) return a + b;
    else return b + a;
  }
}
int main(int argc, const char *argv[])
{
  int i,j,t;
  pair<pII, int> x;
  int a, b, c;
  int tn;
  int n, r, p, s;
  bool flag;
  
  for(i = 0; i < 13; i++){
      if(i==0){
        Win[0] = pair<pII, int> (pII(1, 0), 0);
      }else{
        x = Win[i-1];
        a = x.first.first;
        b = x.first.second;
        c = x.second;
        Win[i] = pair<pII, int>(pII(a+c, b+a), c+b);
      }
  }
  int arr[3];
  cin >> tn;
  for (t = 1; t <= tn; t++) {
    printf("Case #%d: ", t);
    scanf("%d", &n);
    cin >> arr[0] >> arr[2] >> arr[1];
    flag = false;
    if(arr[0] == Win[n].first.first && arr[1] == Win[n].first.second)
      cout << dfs(0, n) << "\n";
    else if( arr[1] == Win[n].first.first && arr[2] == Win[n].first.second)
      cout << dfs(1, n) << "\n";
    else if( arr[2] == Win[n].first.first && arr[0] == Win[n].first.second)
      cout << dfs(2, n) << "\n";
    else 
      puts("IMPOSSIBLE");
  }
  
  return 0;
}
