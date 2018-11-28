#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int test=1;test<=T;test++){
    int A,B,K;
    int poss=0;
    cin >> A >> B >> K;
    for(int i=0;i<A;i++){
      for(int j=0;j<B;j++){
	if((i&j)<K){
	  poss+=1;
	}
      }
    }
    printf("Case #%d: %d",test,poss);
    cout << endl;
  }
  return 0;
}