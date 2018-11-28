#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
int T;
cin>>T;
for (int t=1;t<=T;t++) {
	int N;
	cin>>N;
  vector<int> A(N);
  vector<int> B(N);
  vector<int> X(N,0);
  for (int i=0;i<N;i++){
    cin>>A[i];
  }
  for (int i=0;i<N;i++){
    cin>>B[i];
  }
  for (int x=1;x<=N;x++) {
    int sofar=0;



    for (int i=0;i<N;i++) {
      if (X[i]!=0) {
        if (sofar<A[i]) {
          sofar = A[i];
        }
        continue;
      }
      if ((sofar+1) == A[i]) {
        X[i] = x;
      }
    }
/*
    for (int i=0;i<N;i++){
      cout<<X[i]<<' ';
    }
    cout<<endl;
*/
    sofar = 0;
    int done = -1;
    int maxfront = N+1;
    for (int i=N-1;i>=0;i--) {
      if (X[i]==0) {
        continue;
      }
      if (X[i]<x) {
        if (sofar<B[i])
          sofar = B[i];
      }
      if (X[i]==x) {
        if (sofar+1 == B[i]) {
          if (A[i]>=maxfront) {
            continue;
          }
          done = i;
          maxfront = A[i];
        }
        else {
          X[i]=0;
        }
      }
    }  
    for (int i=0;i<N;i++) {
      if (X[i]==x && done != i) {
        X[i]=0;
      }
    }
  }
  cout<<"Case #"<<t<<": ";
  for (int i=0;i<N;i++) {
    cout<<X[i]<<' ';
  }
  cout<<endl;
}
}
