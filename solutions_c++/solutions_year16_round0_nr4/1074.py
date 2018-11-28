#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string.h>
using namespace std;
char odd[55];
char even[55];
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t,ca;
    scanf("%d",&t);
  for(ca=1;ca<=t;ca++)
      {
      int s,k,c;
      scanf("%d%d%d",&k,&c,&s);
      printf("Case #%d:",ca);
      int i;
      for(i=1;i<=k;i++)printf(" %d",i);
      printf("\n");
  }
    return 0;
}
