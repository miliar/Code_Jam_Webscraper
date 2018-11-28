#include<bits/stdc++.h>

using namespace std;

int main(){

  int T, cases = 1;
  cin>>T;
  while(T--){
    int K, C, S, nedded = -1;
    unsigned long long int Kc = 1;

    cin>>K>>C>>S;

    if(C > K)
      nedded = 1;
    else
      nedded = ceil((double)K / C);
    
    if(S < nedded)
      cout<<"Case #"<<cases++<<": IMPOSSIBLE"<<endl;
    else{

      vector<unsigned long long int> res;
      unsigned long long int start = 0, end = 0, block_size = 0, offset = 1;
      int position = 1;

      cout<<"Case #"<<cases++<<": ";
      for(int i = 1; i <= K; i++){
	cout<<i;
	if(i < K)
	  cout<<" ";
      }
      cout<<endl;
    }
    
  }

  return 0;
}
