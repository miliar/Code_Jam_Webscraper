#include <stdio.h>
#include <algorithm>
#include <functional> 

void deleteElem(float a[], int j, int n){

  for (int i = j; i < n - 1; i++ ){
    a[i] = a[i+1];
  }
  
}


int war(float Naomi[], float Ken[], int n){
  float diff;
  int index; 
  int n2 = n;
  int wins = 0;
  
  for (int i = 0; i < n; i++){
    diff = Ken[0] - Naomi[i];
    index = 0;
    
    for(int j = 0; j < n2; j++){
      if ((diff > Ken[j] - Naomi[i])  && (Ken[j] - Naomi[i] > 0)){
        diff = Ken[j] - Naomi[i];
        index = j;
      }
    }
    if (diff > 0){
      deleteElem(Ken,index,n2);
      n2 -=1;
      continue; 
    }
    diff = 0;
    for(int j = 0; j < n2; j++){
      if (diff > Ken[j] - Naomi[i]){
        diff = Ken[j] - Naomi[i];
        index = j;
      }
    }
    if (diff < 0){
      deleteElem(Ken,index,n2);
      n2 -=1;
      wins++;
      continue; 
    }
    
  }

  return wins; 
}

int dwar(float Ken[], float Naomi[], int n){
  float diff;
  int index; 
  int n2 = n;
  int wins = 0;
  
  for (int i = 0; i < n; i++){
    diff = Naomi[0] - Ken[i];
    index = 0;
    
    for(int j = 0; j < n2; j++){
      if ((diff < Naomi[j] - Ken[i])  && (Naomi[j] - Ken[i] > 0)){
        diff = Naomi[j] - Ken[i];
        index = j;
      }
    }
    if (diff > 0){
      deleteElem(Naomi,index,n2);
      n2 -=1;
      wins++;
      continue; 
    }

    diff = Naomi[0] - Ken[i];
    index = 0;  
    for(int j = 0; j < n2; j++){
        
       if ((diff > Naomi[j] - Ken[i]) && (Naomi[j] - Ken[i] < 0)){
        diff = Naomi[j] - Ken[i];
        index = j;
      }
    }
    if (diff < 0){
      deleteElem(Naomi,index,n2);
      n2 -=1;
      continue; 
    }
    
  }

  return wins; 
}

int main()
{
   int t,n;  
   float naomi[1000];
   float naomi2[1000]; 
   float ken[1000]; 
   float ken2[1000];
   scanf("%d",&t);
   
   for (int i = 1; i <= t; i++){
    scanf("%d",&n);
    for (int j = 0; j < n; j++){
      scanf("%f",&naomi[j]);
      naomi2[j] = naomi[j];
      
    }
    for (int j = 0; j < n; j++){
      scanf("%f",&ken[j]); 
      ken2[j] = ken[j];
    }
   
    std::sort(ken, ken + n, std::greater<float>());
    
    int w = war(naomi,ken,n);
    
    std::sort(ken2, ken2 + n, std::greater<float>());
    
    
    int dw = dwar(ken2,naomi2,n);
    
    printf("Case #%d: %d %d\n", i,dw,w); 
   
   };
  

   return 0;
}
