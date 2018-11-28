#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

template<class T>
void answer(int Case, T ans){
  cout << "Case #" << Case << ": " << ans << endl;
}

int main(){
  cout.precision(7);
  cout << std::fixed;

  int T;
  cin >> T;
  for(int Case=1;Case<=T;++Case){
	double C, F, X;
	cin >> C >> F >> X;

	int n = std::max(0.0, ceil(X/C - 2.0/F - 1));

	double time=0;
	for(int i=n-1;i>=0;--i){
	  time += C/(2+i*F);
	}
	time += X/(2+n*F);
	
	answer(Case, time);
  }
}
