#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <queue>

#include <NTL/ZZ.h>
using namespace NTL;

using namespace std;

ZZ get_max(ZZ N,ZZ p){

  if(p==to_ZZ(1)){
    return to_ZZ(0);
  }
  ZZ rem = N/2;
  ZZ ans = rem;
  ZZ D=to_ZZ(4);
  while(p>=D){
    D*=2;
    rem /= 2;
    ans += rem;
  }

  return ans;
}

ZZ get_min(ZZ N,ZZ p){

  return N-get_max(N,p)-1;

}


int main(){

	int i_cases;
	int N_cases;

	cin>>N_cases;

	for(i_cases=0;i_cases<N_cases;i_cases++){

	  int N;
	  ZZ P;

	  cin>>N>>P;

	  ZZ N2 = power2_ZZ(N);

	  ZZ M = get_max(N2,P);
	  ZZ m = get_min(N2,N2-P)-1;
	  
	  if(P==N2){
	    m = N2-1;
	  }

	  cout<<"Case #"<<i_cases+1<<": "<<m<<" "<<M<<endl;


	}
	return 0;

}
