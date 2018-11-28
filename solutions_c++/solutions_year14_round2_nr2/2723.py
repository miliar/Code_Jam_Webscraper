#include <stdio.h>
#include <algorithm>
#include <functional>
#include <iostream> 

int lot(int a, int b, int k){
  
  int n =0;
  for(int i = 0; i < a; i++){
  
    for(int j = 0; j < b; j++){
      int m;
      m = i&j;
      if (m<= k-1){
        n++;
      }
  
  }
  
  }

  return n;
}


int main()
{
   int t,a,b,k;  
   scanf("%d", &t);
   
   for (int i = 1; i <= t; i++){
    scanf("%d %d %d",&a,&b,&k);
    
    int l = lot(a,b,k);
    printf("Case #%d: %d\n",i,l); 
   
   };
  

   return 0;
}
