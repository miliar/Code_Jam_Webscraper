#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

int main(){
  int casos,ca = 0;
  int r,t,cont,acum;
  scanf("%i",&casos);
  while(casos--){
    scanf("%i %i",&r,&t);
    acum = 0;
    cont = 0;
    for(int i = r; t > 0; i+= 2){
      t -= ((1+i)*(i+1)) - (i*i);
      cont++;
    }
    if(t<0) cont--;
    printf("Case #%i: %i\n",++ca,cont);
  }
  return 0;
}