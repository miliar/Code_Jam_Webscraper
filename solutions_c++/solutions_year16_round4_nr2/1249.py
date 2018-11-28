#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int T, N, K;
  cin >> T;
  for (int x=1; x<=T; x++) {
    cin >> N >> K;
    double P[N], answer = 0.0;
    for (int i=0; i<N; i++) cin >> P[i];
    for (int S=0; S<(1<<N); S++) {
      int k=0; 
      for (int Stmp=S; Stmp; Stmp>>=1) if (Stmp&1) k++;
      if (k==K) { // correct subset size
	double Pyes[K+1];
	Pyes[0]=1.0;
	k=0;
	for (int i=0; i<N; i++)
	  if ((S>>i)&1) {
	    k++;
	    Pyes[k]=Pyes[k-1]*P[i];
	    for (int j=k-1; j>0; j--) 
	      Pyes[j]=Pyes[j]*(1.0-P[i]) + Pyes[j-1]*P[i];
	    Pyes[0] = Pyes[0]*(1.0-P[i]);
	    /*
	    for (int j=0; j<=k; j++) cout << P[j] << " ";
	    cout << endl;
	    */	    
	  };
	if (Pyes[K/2]>answer) answer = Pyes[K/2];
      };
    };
    cout << setprecision(10) << "Case #" << x << ": " << answer << endl;
  };
  return 0;
};
