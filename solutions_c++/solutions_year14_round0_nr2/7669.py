#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

  int T;
  double C,F,X; 
    
  cin >> T;


  for(int t=1; t<=T; t++){
    
    cin >> C >> F >> X;

    double latest_res = X/2;

    for(int f=1;;f++){

      double res = 0;
      
      for(int i=0;i<f;i++){
        res += C/( (F*i) + 2 );
      }
      res += X/ ((F*f) + 2 );

      if(res >= latest_res)
        break;

      latest_res = res;

    }

    printf("Case #%d: %.7f\n",t,latest_res);  
  }

  return 0;
}

