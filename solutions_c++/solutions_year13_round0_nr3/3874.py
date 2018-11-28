#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main(){

  int palis[] = {1,4,9,121,484,10201,12321,14641,40804,44944};
  int size = 10;

  int N,a,b,i,c,t=0;
  cin>>N;
  for(c=1;N--;c++,t=0){
    cin>>a>>b;
    for(i=0;i<size && palis[i] <= b;++i){
      if(palis[i] < a) continue;
      t++;
    }
    printf("Case #%d: %d\n",c,t);
  }
  return 0;
}
