#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
#define lint unsigned long long int

class sol{
public:
  int N,K;
  vector<double> P;
  
  double bestP=0.0;
  void recur(vector<double> e,int i, int k){
    if(k==0){
      bestP=max(bestP,e[K/2]);
    }else if(i==N){
      return;
    }else{
      recur(e,i+1,k);
      for(int j=K;j>0;j--){
	e[j]= P[i]*e[j-1] +  (1-P[i]) * e[j];
      }
      e[0] = (1- P[i])*e[0];
      recur(e,i+1,k-1);
    }
  }


  string solve(){
    cin>>N>>K;
    P.resize(N);
    for(int i=0;i<N;i++)
      cin>>P[i];
    vector<double> e(K+1,0.0);
    e[0]=1;
    recur(e,0,K);
    return to_string(bestP);
  }

};




int main(){
  int N;
  cin>>N;
  for(int i=0;i<N;i++){
    // Leggi
    cout<<"Case #"<<i+1<<": "<<sol().solve()<<endl;
  }

  return 0;
}
