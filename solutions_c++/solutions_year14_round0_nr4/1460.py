#include <stdio.h>
#include <algorithm>

int main(){

  int T;
  scanf("%d", &T);


  for(int k=1; k<=T; k++){
    double Na[1001];
    double Ke[1001];
    
    int N;
    
    scanf("%d", &N);
  
    for(int i =0 ; i<N; i++) scanf("%lf", &Na[i]);
    for(int i =0 ; i<N; i++) scanf("%lf", &Ke[i]);

    
    std::sort(Na, Na+N);
    std::sort(Ke, Ke +N);
  
    //printf("SORT:\n");
    //for(int i=0; i<N; i++) printf("%lf ", Na[i]);
    //printf("\n");

    int nWar = 0;
    int nDwar = 0;

    int indNplus = N-1;
    int indNminus = 1;
    for(int i = N-1; i>=0; i--){
      //printf("%lf %lf\n", Ke[i], Na[indNplus]);
      if( Ke[i] < Na[indNplus]){
	nDwar += 1;
	indNplus --;
      }
      else if(Ke[i]>Na[indNplus]){
	  indNminus ++; 
	}
    }
  
    int ind = 0;
    for(int i = 0; i<N; i++){
      while(ind < N && Ke[ind] < Na[i]){
	ind++;
      }
      
      if(ind <N){  nWar++; ind++;}
      else {break;}
    }

    printf("Case #%d: %d %d\n",k,  nDwar, N-nWar);
  }
  return 0;
}
