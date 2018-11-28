#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

int palindrom(int a) {
  char a_str[30];
  int i, k=sprintf(a_str, "%d", a)-1;
  for(i=0; i<k; i++, k--)
    if(a_str[i] != a_str[k])
      return 0;
  return 1;
}

int main() {
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int C;
  cin >> C;
  int a, b;
  for(int i=0; i<C; i++) {
    cin >> a >> b;
    int cnt = 0;
    for(int j=a, k=b; j<=k; j++)
      if(sqrt(j)==sqrt(float(j) ) && palindrom(sqrt(j) ) && palindrom(j) )
        cnt++;
    cout << "Case #" << i+1 << ": "<< cnt << endl;
  }
  
  return 0;
}

