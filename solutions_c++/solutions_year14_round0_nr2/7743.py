#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(){
  int num_case = 0,i,j,p;
  cin>>num_case;

  long double result[100];
  long double C = 0,F = 0,X = 0;

  for(i=0;i<num_case;i++){
    cin>>C;
    cin>>F;
    cin>>X;

    // compute sum till sum decreases
    long double sum = X/2;
    int k = 0;
    while(1){
      long double temp = 0;
      for(j=0;j<=k;j++){
	temp = temp + C / (2 + F*j);
      }
      
      temp = temp + (X-C) / (2 + F*k);

      if(temp <= sum){
	sum = temp;
	k++;
      }
      else if(temp > sum) break;
    }

    result[i] = sum;        

  }


  for(i=0;i<num_case;i++){
    printf("Case #%d: %.7f\n", i+1, result[i]);
  }


  return 0;
}
