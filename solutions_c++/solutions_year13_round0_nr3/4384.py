#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;
int isPalin(long long int pal){
  int a[16],l=0;
  
  while(pal){
    a[l++] = pal%10;
    pal /= 10;
  }
  for(int i = 0;i<l/2;i++){
    if(a[i] != a[l-i-1])
      return 0;
  }
  return 1;
  
}


int main(){
  int t,n,count;
  long long int i[100000],k,a,b;
  
  n = 0;
  while(i[n-1]<(int)1E14){
    for(long long int l = 1;l<1E7;l++){
      if(isPalin(l) && isPalin(l*l)){
	i[n++] = l*l;
      }
    }   
    
  }
  scanf("%d", &t);
  
  for(int j = 0;j<t;j++){
    scanf("%lld %lld", &a, &b);
    count = 0;
    for(int k = 0;k< 100000;k++){
      if(i[k] > b)
	break;
      if(i[k] >= a && i[k] <= b){
	count++;
      }
	
      
    }
    printf("Case #%d: %d\n", j+1,count);
    
  }
  
 
  return 0;
}
