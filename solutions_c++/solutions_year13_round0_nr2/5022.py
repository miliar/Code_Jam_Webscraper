#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int main(){
  int t;
  int m,n,flag;
  int a[100][100];
  int maxl[100],maxc[100];
  scanf("%d", &t);
  
  for(int l =0;l<t;l++){
    scanf("%d %d", &m, &n);
    for(int i = 0;i<100;i++){
      maxl[i] = 0; maxc[i] = 0;
      for(int j = 0;j<100;j++){
	a[i][j] = 0;
      }
    }
      
    
    for(int i =0;i<m;i++){
      for(int j = 0;j<n;j++){
	scanf("%d", &a[i][j]);
	if(a[i][j] > maxl[i]) maxl[i] = a[i][j];
      }
    }    
    for(int i = 0;i<100;i++){
      for(int j = 0;j<100;j++){
	if(a[j][i] > maxc[i]) maxc[i] = a[j][i];
      }
    }
    
    flag = 0;
    for(int i = 0;i<m;i++){
      for(int j = 0;j<n;j++){
	if(a[i][j] < maxl[i] && a[i][j] < maxc[j]){
	  flag = 1;
	  break;
	}
      }
      if(flag)
	break;
    }
    
    if(!flag)
      printf("Case #%d: YES\n",l+1);
    else
      printf("Case #%d: NO\n",l+1);
    
    
    
  }  
  return 0;
}
