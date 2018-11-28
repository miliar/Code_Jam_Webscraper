#include <iostream>
#include <string>
#include <stdio.h>
#include <set>
using namespace std;
int main()
{
  int T,N;
  scanf("%d",&T);
  set<int> set;
  for(int i=0;i<T;i++){
      scanf("%d",&N);
      printf("Case #%d: ");
      if(N==0) printf("INSOMNIA\n");
      else{
          int j =1;
        while(set.size()<10){
            int tmp = j*N;
            while(tmp >0){
                int x = tmp%10;
            set.insert(x);
            tmp =tmp/ 10;
            }
            j++;
        }
        j--;
        printf("%d\n",j*N);
        set.clear();
      }
      
  }
}
