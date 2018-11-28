#include<bits/stdc++.h>

using namespace std;

int main(){

  int T, cases = 1;
  char side;

  cin>>T;
  
  getchar();
  while(T--){
    int S[105] = {0}, i = 0, res = 0, state = -1;
    //int state_start = 0, state_end = 0, inverse_start = 0, inverse_end = 0;

    side = getchar();
    while(side != '\n'){
      if(side == '-')
	S[i] = 0;
      else if(side == '+')
	S[i] = 1;
      i++;
      side = getchar();
    }

    state = S[0];
    for(int k = 1; k < i; k++){
      if(S[k] != state){
	state = 1  - state;
	res++;
      }
    }
    if(state == 0)
      res++;
    cout<<"Case #"<<cases++<<": "<<res<<endl;
  }  
  
  return 0;
}
