#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;



void openFile(){
  freopen("C-small-attempt0.in","r",stdin);
  freopen("C-small-attempt0.out","w",stdout);
}

bool is_palindrome(int n){
  vector<int> vt;
  while(n > 0){
    vt.push_back(n%10);
    n /= 10;
  }
  int sz = vt.size();
  for(int i = 0; i < (sz+1)/2; i++){
    if(vt[i] != vt[sz-1-i])return false;
  }
  return true;
}

int find(int from){
  int s = (int)sqrt(from);
  if(s * s < from)
    return s + 1;
  return s;
}

int main(){
  openFile();
  int ncase;
  int n, c;
  int no = 0;
  int from, to;
  scanf("%d", &ncase);

  while(ncase > no){
    no++;
    scanf("%d %d",&from, &to);
    int ans = 0;
    int i = find(from);
    for( ; i*i <= to; i++){
      if(is_palindrome(i) && is_palindrome(i*i))ans++;
    }
    printf("Case #%d: %d\n", no, ans);
  }
  return 0;
}
