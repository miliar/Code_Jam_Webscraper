#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int main()
{
  int T;
  char S[109];
  char* p;
  int count =0;
  scanf("%d",&T);
  for(int i=0;i<T;i++){
      count =0;
      bool stateplus = 1;
    cin >> S;
    p = S;
    while(*p != '\0') p++;
    p--;
    while(*p != '\0'){
        if(stateplus == 1 && *p == '-') {
            count++;
            stateplus = 0;
        }
        else if(stateplus ==0 && *p =='+') {
            count++;
            stateplus = 1;
        }
        p--;
    }
    printf("Case #%d: %d\n",i+1,count);
  }
}
