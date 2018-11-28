#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>


using namespace std;


int main(){
  long long int r,t,k;	
  int n,som;
  
  scanf("%d", &n);
  
  for(int i = 0;i<n;i++){
    som = 0;
    scanf("%lli %lli", &r, &t);
    r++;
    while(t>0){
      k = (2*r-1);
      if(k>t)
	break;
      som++;
      t-=k;
      r+=2;
    }
      
    
    printf("Case #%d: %d\n",i+1,som);
    
    
  }
  
  return 0;

}
